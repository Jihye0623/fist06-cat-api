import requests
import os

# 1. 고양이 사진 URL 가져오기 (The Cat API)
def get_cat_url():
    url = "https://api.thecatapi.com/v1/images/search"
    try:
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            return data[0]['url'] # 이미지 주소 반환
        else:
            print("API 호출 실패")
            return None
    except Exception as e:
        print(f"에러 발생: {e}")
        return None

# 2. README 파일 업데이트하기
def update_readme(image_url):
    file_path = "README.md"
    
    # 파일 읽기
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()

    # 사진이 들어갈 위치 찾기 (마커 기준)
    start_marker = ""
    end_marker = ""
    
    start_index = content.find(start_marker)
    end_index = content.find(end_marker)

    if start_index == -1 or end_index == -1:
        print("README에서 마커를 찾을 수 없습니다! 와 를 확인하세요.")
        return

    # 새로운 내용 조합 (기존 마커는 유지하고 가운데 img 태그만 교체)
    new_content = (
        content[:start_index + len(start_marker)] + "\n" +
        f'<img src="{image_url}" width="400">' + "\n" +
        content[end_index:]
    )

    # 파일 저장
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(new_content)
    print(f"새로운 고양이 사진으로 업데이트 완료! : {image_url}")

if __name__ == "__main__":
    img_url = get_cat_url()
    if img_url:
        update_readme(img_url)