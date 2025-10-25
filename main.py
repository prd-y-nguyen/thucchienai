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
# TRANG 4 - YÊU CẦU THÔNG TIN CÁ NHÂN

## THÔNG TIN TRANG
**Số trang:** 4
**Số khung:** 4 khung
**Màu sắc:** Trắng đen

${style_prompt}
${minh_prompt}

## KHUNG 1 - YÊU CẦU THÔNG TIN
**Kích thước:** Trung bình (30% trang)
**Vị trí:** Góc trên trái

**Tin nhắn:**
- Nội dung: "Để nhận phần thưởng, bạn cần cung cấp thông tin tài khoản game và số điện thoại"
- Emoji: 📱 🎮
- Style: Lịch sự, chuyên nghiệp giả tạo

---

## KHUNG 2 - YÊU CẦU CHUYỂN TIỀN
**Kích thước:** Trung bình (30% trang)
**Vị trí:** Góc trên phải

**Tin nhắn:**
- Nội dung: "Sau đó chuyển khoản 200k vào số tài khoản này để đặt cọc"
- Số tài khoản: "123 456 7890"
- Emoji: 💵 ✨

---

## KHUNG 3 - MINH VUI MỪNG
**Kích thước:** Lớn (40% trang)
**Vị trí:** Dưới hai khung trên

**Nhân vật MINH:**
- Biểu cảm: Vui mừng, phấn khích, miệng cười lớn
- Tư thế: Đứng dậy hoặc ngồi thẳng
- Ngôn ngữ cơ thể: Tích cực, năng lượng cao

**Thought bubble:** "Mình sắp có tất cả skin rồi!"

---

## KHUNG 4 - MINH CHẠY ĐI TÌM LAN
**Kích thước:** Nhỏ (30% trang)
**Vị trí:** Góc dưới phải

**Nhân vật MINH:**
- Hành động: Đang chạy, tay vung cao cầm điện thoại
- Biểu cảm: Phấn khích, háo hức
- Background: Phòng ngủ → hành lang (chuyển cảnh)

**Speech bubble:** "Lan ơi! Có tin vui!"

## BỐ CỤC
- Khung 1-2: Tin nhắn (bố cục song song)
- Khung 3: Phản ứng của Minh
- Khung 4: Hành động, dẫn đến trang tiếp theo

## TONE
**Cảm xúc:** Đồng ý → Vui mừng → Hào hứng
**Mục tiêu:** Cho thấy Minh đã tin và sẵn sàng thực hiện

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