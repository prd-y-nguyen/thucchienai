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
# TRANG 3 - TIN NHẮN LỪA ĐẢO

## THÔNG TIN TRANG
**Số trang:** 3
**Số khung:** 4 khung
**Màu sắc:** Trắng đen
**Kích thước:** A4

${style_prompt}
${minh_prompt}

## KHUNG 1 - MINH MỞ TIN NHẮN
**Kích thước:** Lớn (50% trang)
**Vị trí:** Trên cùng

**Bối cảnh:** Cận cảnh điện thoại, giao diện Facebook Messenger đang mở

**Nhân vật MINH:** (Chỉ thấy tay và điện thoại trong khung)
- Tay cầm điện thoại, ngón tay chạm màn hình

**Tin nhắn hiển thị:**
- Avatar người gửi: Ảnh đại diện mặc định hoặc mờ
- Tên: "Support Game" hoặc tên khó đọc
- Nội dung: "Bạn có cơ hội nhận TẤT CẢ skin trong game!"
- Style: Chữ lớn, in đậm, màu sắc sặc sỡ

---

## KHUNG 2 - YÊU CẦU ĐẶT CỌC
**Kích thước:** Trung bình (30% trang)
**Vị trí:** Dưới khung 1, bên phải

**Tin nhắn tiếp theo:**
- Nội dung: "Chỉ cần đặt cọc 200k để làm thủ tục nhận thưởng ngay!"
- Emoji: 💰 💎 ⚡
- Style: Nhiều màu sắc, hấp dẫn

---

## KHUNG 3 - MINH HỎI LẠI
**Kích thước:** Nhỏ (20% trang)
**Vị trí:** Dưới khung 2

**Tin nhắn của MINH:**
- Avatar Minh: Ảnh rõ ràng
- Nội dung: "Tất cả skin ư? Thật không?"
- Biểu cảm (nếu có avatar): Ngạc nhiên, hoài nghi nhẹ

---

## KHUNG 4 - PHẢN HỒI KẺ LỪA ĐẢO
**Kích thước:** Trung bình (30% trang)
**Vị trí:** Góc dưới bên phải

**Tin nhắn của kẻ lừa đảo:**
- Nội dung: "Đúng vậy! Cơ hội chỉ trong nháy mắt, nhanh lên!"
- Emoji: ⏰ ⚡ 🔥
- Style: Nhiều biểu tượng, tạo cảm giác khẩn trương

## MÀU SẮC VÀ TONE
- Background: Trắng
- Tin nhắn: Nhiều màu sắc (trong phong cách trắng đen thì dùng độ đậm nhạt khác nhau)
- Tạo cảm giác gấp gáp và hấp dẫn

## THÔNG ĐIỆP
**Tone:** Hấp dẫn → Hoài nghi → Áp lực
**Mục tiêu:** Cho thấy cách kẻ lừa đảo dụ dỗ và tạo áp lực thời gian

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