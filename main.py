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
# TRANG 1 - TRANG BÌA (MÀU)

## THÔNG TIN TRANG
**Số trang:** 1
**Loại:** Trang bìa
**Màu sắc:** Màu (color)
**Kích thước:** A4

${style_prompt}
${minh_prompt}

## TIÊU ĐỀ VÀ NỘI DUNG VĂN BẢN
**Tiêu đề chính:** "CẢNH BÁO LỪA ĐẢO GAME ONLINE"
**Phụ đề:** "Đừng để bị dụ dỗ bởi những lời hứa hão huyền!"
**Màu tiêu đề:** Đỏ cảnh báo (#FF0000), font chữ lớn, in đậm
**Màu phụ đề:** Đen hoặc xám đậm, font chữ nhỏ hơn

## PROMPT HÌNH ẢNH CHI TIẾT

### Bối cảnh chính:
Dark dramatic scene with menacing atmosphere. Dark background (deep purple/black gradient) representing the dangerous digital world. Floating digital elements and glowing warning signs in the background.

### Nhân vật chính - MINH:
16-year-old Vietnamese male student sitting on floor or chair, playing mobile game on smartphone. Expression: innocent, unaware of danger, focused on the game. Wearing casual clothes (t-shirt and jeans). Short black hair, kind but naive expression. The smartphone screen glows brightly.

### Các pop-up Facebook (trừu tượng):
Floating Facebook notification bubbles and pop-up windows around Minh, showing fake messages like "Trúng giải skin!", "Nhận tất cả skin miễn phí!", "Chúc mừng! Bạn là người may mắn!", "Đặt cọc 200k nhận ngay!". These pop-ups have warning red colors and suspicious appearance.

### Bóng đen (Kẻ lừa đảo):
Sinister dark silhouette or shadowy figure emerging from the smartphone screen, reaching towards Minh with claw-like hands. The figure is faceless, ominous, representing the online scammer. Glowing red eyes visible. Menacing posture, clearly predatory.

### Yếu tố cảnh báo:
Warning symbols floating in the background: skull and crossbones, exclamation marks, stop signs. Red warning lights and digital glitch effects.

## MÀU SẮC TỔNG THỂ
- Nền tối: Tông màu tím đen hoặc đen sâu (#1a1a2e, #0f0f1e)
- Điểm nhấn đỏ: Các yếu tố cảnh báo màu đỏ rực (#ff0000, #ff3333)
- Nhân vật: Màu tự nhiên, da người (#ffdbac), tóc đen
- Điện thoại: Màn hình xanh phát sáng (#00ffff)
- Pop-up: Màu vàng/cam cảnh báo (#ffaa00, #ff8800)

## COMPOSITION (BỐ CỤC)
- Trung tâm: Minh đang chơi game
- Tiêu đề: Ở phía trên cùng, nổi bật
- Phụ đề: Ngay dưới tiêu đề chính
- Bóng đen: Vươn ra từ phía sau Minh, tạo không khí đe dọa
- Pop-up: Rải rác xung quanh, tạo cảm giác bị bao vây

## TONE VÀ THÔNG ĐIỆP
**Cảm xúc:** Cảnh báo, căng thẳng, nguy hiểm tiềm ẩn
**Thông điệp:** Sự ngây thơ có thể dẫn đến nguy hiểm trực tuyến
**Mục tiêu:** Thu hút sự chú ý, tạo ấn tượng mạnh về nguy cơ lừa đảo game online

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