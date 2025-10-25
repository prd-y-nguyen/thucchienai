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
A 16-year-old Vietnamese high school student, male, average height, friendly and approachable appearance. Wearing casual school uniform (white shirt, dark blue pants) or casual clothes (t-shirt and jeans). Short black hair, kind eyes, slightly naive expression. Clean and neat appearance typical of a good student.
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
# TRANG 2 - GIỚI THIỆU NHÂN VẬT

## THÔNG TIN TRANG
**Số trang:** 2
**Số khung:** 4 khung
**Màu sắc:** Trắng đen
**Kích thước:** A4

${style_prompt}
${minh_prompt}

## KHUNG 1 - MINH ĐANG CHƠI GAME
**Kích thước:** Lớn (40% trang)
**Vị trí:** Góc trên trái

**Bối cảnh:** Phòng ngủ của Minh, gọn gàng, có bàn học, giường, cửa sổ có ánh sáng tự nhiên

**Nhân vật MINH:**
- Tư thế: Ngồi thoải mái trên giường/ghế
- Ngoại hình: 16 tuổi, nam, tóc đen ngắn
- Trang phục: Áo phông trơn, quần jeans
- Biểu cảm: Tập trung, vui vẻ, mắt dán vào màn hình
- Hành động: Hai tay cầm điện thoại, chân bắt chéo thoải mái

**Chi tiết điện thoại:** Màn hình hiển thị game Liên Quân Mobile với đồ họa sáng

---

## KHUNG 2 - TIN NHẮN FACEBOOK
**Kích thước:** Nhỏ (20% trang)
**Vị trí:** Góc trên phải

**Hình ảnh:** Cận cảnh điện thoại với thông báo Facebook Messenger:
- Logo Facebook xanh
- Nội dung: "Chúc mừng! Bạn là người may mắn!"
- Avatar người gửi mặc định
- Thời gian: "vừa xong"

---

## KHUNG 3 - PHẢN ỨNG MINH
**Kích thước:** Trung bình (30% trang)
**Vị trí:** Giữa trang bên trái

**Nhân vật MINH:**
- Biểu cảm: Ngạc nhiên, tò mò, mắt mở to, lông mày nhướn lên, miệng hơi mở
- Tư thế: Ngả người về phía trước, đưa điện thoại gần mặt
- Ngôn ngữ cơ thể: Thể hiện quan tâm, mong đợi

**Background:** Làm mờ phòng ngủ

---

## KHUNG 4 - SUY NGHĨ CỦA MINH
**Kích thước:** Nhỏ (10% hoặc thought bubble)
**Vị trí:** Cloud từ khung 3

**Thought bubble:** 
- Hình dáng: Đám mây suy nghĩ mềm mại
- Nội dung: "Thật không? Mình trúng giải sao?"
- Yếu tố hình ảnh: Dấu hỏi nhỏ, sao vàng, skin game

**Màu:** Đen trắng với shading tinh tế

## BỐ CỤC TỔNG THỂ
Flow: Trái → phải, trên → dưới
Nhịp điệu: Khung 1 lớn giới thiệu → Khung 2 nhỏ điểm nhấn → Khung 3 phản ứng → Khung 4 suy nghĩ

## MÀU SẮC
- Background: Trắng
- Line art: Đen
- Shading: Tông xám

## TONE VÀ THÔNG ĐIỆP
**Cảm xúc:** Bình yên → tò mò → kỳ vọng
**Mục tiêu:** Thiết lập tình huống và sự ngây thơ

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