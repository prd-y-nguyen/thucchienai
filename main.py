from openai import OpenAI
import base64
import random

# --- Cấu hình ---
AI_API_BASE = "https://api.thucchien.ai/v1"
AI_API_KEY = "sk-7do3XH4YVScPXSqiW5YJ3w"

# --- Khởi tạo client ---
client = OpenAI(
  api_key=AI_API_KEY,
  base_url=AI_API_BASE
)

style_prompt = """

## STYLE VÀ KỸ THUẬT VẼ

### Phong cách tổng thể:
```
Manga/Anime style, clean line art, suitable for educational comic. Bright and clear illustrations. Professional comic book style with clear character expressions and body language. Black and white for content pages, colorful for cover page.
```

### Màu sắc:
- **Trang bìa:** Tông màu tối với điểm nhấn đỏ cảnh báo
- **Trang nội dung:** Trắng đen với tông xám
- **Nhân vật:** Màu da tự nhiên, tóc đen, quần áo đơn giản
- **Cảnh báo:** Màu đỏ cho các yếu tố nguy hiểm

### Kỹ thuật vẽ:
```
Clean line art, clear panel composition, easy to read expressions. Educational comic style with emphasis on clarity and understanding. Professional manga/anime illustration quality.
```
"""

minh_prompt = """
### 1. MINH (16 tuổi) - Nhân vật chính
**Mô tả tổng quan:**
```
A 16-year-old Vietnamese high school student, male, average height, friendly and approachable appearance.
Black short hair.
Wearing casual school uniform (white shirt, dark blue pants).
Short black hair, kind eyes, slightly naive expression. Clean and neat appearance typical of a good student.
```

**Các biểu cảm cần thiết:**
- **Ngạc nhiên:** "Surprised expression, wide eyes, mouth slightly open, eyebrows raised"
- **Vui mừng:** "Happy and excited expression, bright smile, eyes sparkling"
- **Do dự:** "Hesitant expression, furrowed brow, uncertain look, hand on chin"
- **Bối rối:** "Confused expression, tilted head, questioning look"
- **Cảm ơn:** "Grateful expression, warm smile, nodding head"
- **Tự tin:** "Confident expression, determined look, standing tall"
"""

lan_prompt = """
### 2. LAN (16 tuổi) - Bạn thân, người hướng dẫn
**Mô tả tổng quan:**
```
A 16-year-old Vietnamese high school student, female, intelligent and confident appearance. Wearing school uniform (white blouse, dark blue skirt) or casual clothes. Shoulder-length black hair, sharp and alert eyes, mature and knowledgeable expression. Carries herself with confidence and wisdom beyond her years.
```

**Các biểu cảm cần thiết:**
- **Cảnh báo:** "Urgent and concerned expression, pointing finger, serious look"
- **Giải thích:** "Patient and teaching expression, gentle smile, hands gesturing"
- **Tự tin:** "Confident and authoritative expression, standing straight, determined look"
- **Khuyến khích:** "Encouraging expression, warm smile, supportive gesture"
"""

khe_lua_dao_prompt = """

### 3. KẺ LỪA ĐẢO (Giọng nói qua điện thoại)
**Mô tả:**
```
A shadowy figure or silhouette representing online scammers. Dark, mysterious appearance with hidden face. Wearing formal business attire (suit) to appear legitimate. Menacing presence with predatory posture. Can be shown as a dark silhouette with glowing eyes or as a figure with phone/computer.
```

**Các biểu cảm:**
- **Thuyết phục:** "Persuasive and manipulative expression, fake smile, leaning forward"
- **Áp lực:** "Urgent and pressuring expression, pointing finger, aggressive posture"
- **Thất bại:** "Frustrated and angry expression, clenched fists, defeated look"

"""

friend_prompt = """
### 4. CÁC BẠN HỌC SINH TRONG LỚP
**Mô tả:**
```
Group of Vietnamese high school students (ages 14-17), diverse group with both male and female students. Wearing school uniforms or casual clothes. Various expressions of attention, curiosity, and engagement. Sitting in classroom setting, some taking notes, others listening attentively.
```
"""

prompt = """
You are an manga artist.

Your job is to draw an page with these information:
# TRANG 7 - CÁC DẤU HIỆU LỪA ĐẢO

## THÔNG TIN TRANG
**Số trang:** 7
**Số khung:** 4 khung

${style_prompt}
${minh_prompt}
${lan_prompt}

## KHUNG 1 - DẤU HIỆU 1
**Kích thước:** Trung bình (25% trang)
**Vị trí:** Góc trên trái

**Nhân vật LAN:**
- Biểu cảm: Giáo dục, chỉ số 1
- Tư thế: Tay chỉ lên

**Visual:** Số "1" lớn, icon tin nhắn

**Speech bubble LAN:** "Dấu hiệu 1: Tin nhắn trúng giải bất ngờ qua Facebook"

---

## KHUNG 2 - DẤU HIỆU 2
**Kích thước:** Trung bình (25% trang)
**Vị trí:** Góc trên phải

**Nhân vật LAN:**
- Biểu cảm: Tiếp tục liệt kê
- Tư thế: Tay chỉ số 2

**Visual:** Số "2" lớn, icon tiền mặt

**Speech bubble LAN:** "Dấu hiệu 2: Yêu cầu đặt cọc hoặc chuyển tiền để nhận thưởng"

---

## KHUNG 3 - DẤU HIỆU 3
**Kích thước:** Trung bình (25% trang)
**Vị trí:** Góc dưới trái

**Nhân vật LAN:**
- Biểu cảm: Tiếp tục
- Tư thế: Tay chỉ số 3

**Visual:** Số "3" lớn, icon đồng hồ

**Speech bubble LAN:** "Dấu hiệu 3: Tạo áp lực thời gian, bắt phải quyết định nhanh"

---

## KHUNG 4 - DẤU HIỆU 4
**Kích thước:** Trung bình (25% trang)
**Vị trí:** Góc dưới phải

**Nhân vật LAN:**
- Biểu cảm: Kết thúc liệt kê
- Tư thế: Tay chỉ số 4

**Visual:** Số "4" lớn, icon tin nhắn riêng

**Speech bubble LAN:** "Dấu hiệu 4: Không có tài khoản chính thức, chỉ liên hệ qua tin nhắn riêng"

## BỐ CỤC
- Bố cục lưới 2x2
- Mỗi khung có số và icon rõ ràng
- Đồng nhất về phong cách

## TONE
**Thông tin:** Giáo dục, hệ thống
**Mục tiêu:** Liệt kê rõ ràng các dấu hiệu

"""

# --- Gọi API để tạo hình ảnh ---
response = client.images.generate(
  model="imagen-4",
  prompt=prompt + str(random.randint(1, 10000)),
  n=1,
  size="1024x1792",
  output_format="png"
)

# --- Xử lý và lưu từng ảnh ---
for i, image_obj in enumerate(response.data):
  b64_data = image_obj.b64_json
  image_data = base64.b64decode(b64_data)

  save_path = f"generated_image_{i+1}.png"
  with open(save_path, 'wb') as f:
      f.write(image_data)
  print(f"Image saved to {save_path}")