# Xenweb-Telegram-BOT-1
Multilingual Telegram bot for ordering digital services (website design, bot development, SEO, graphic design, etc.) with dedicated admin panel

<div dir="rtl" align="right">

![Python Version](https://img.shields.io/badge/python-3.7%2B-blue)
![Telegram Bot](https://img.shields.io/badge/telegram-bot-blue)
![License](https://img.shields.io/badge/license-MIT-green)
![Version](https://img.shields.io/badge/version-1.0.0-orange)

</div>

---

## 📋 Table of Contents / فهرست مطالب

- [Introduction / معرفی](#introduction--معرفی)
- [Features / ویژگی‌ها](#features--ویژگیها)
- [Demo / دمو](#demo--دمو)
- [Prerequisites / پیش‌نیازها](#prerequisites--پیشنیازها)
- [Installation / نصب](#installation--نصب)
- [Configuration / تنظیمات](#configuration--تنظیمات)
- [Usage / نحوه استفاده](#usage--نحوه-استفاده)
- [Admin Panel / پنل ادمین](#admin-panel--پنل-ادمین)
- [Database Structure / ساختار دیتابیس](#database-structure--ساختار-دیتابیس)
- [API Reference / مرجع توابع](#api-reference--مرجع-توابع)
- [Troubleshooting / عیب‌یابی](#troubleshooting--عیبیابی)
- [Contributing / مشارکت](#contributing--مشارکت)
- [License / لیسانس](#license--لیسانس)
- [Contact / تماس](#contact--تماس)

---

## 📝 Introduction / معرفی

<div dir="rtl" align="right">

**ربات Xenweb** یک ربات تلگرام قدرتمند و چندزبانه برای مدیریت خدمات دیجیتال است. این ربات با زبان پایتون نوشته شده و با استفاده از کتابخانه `pyTelegramBotAPI` ارتباط با تلگرام را برقرار می‌کند. این ربات برای کسب‌وکارها و فریلنسرهایی که خدمات دیجیتال متنوع ارائه می‌دهند طراحی شده است.

</div>

**Xenweb Bot** is a powerful multilingual Telegram bot for managing digital services. Written in Python, it uses the `pyTelegramBotAPI` library to communicate with Telegram. This bot is designed for businesses and freelancers offering various digital services.

### 🎯 Main Applications / کاربردهای اصلی

<div dir="rtl" align="right">

- ثبت سفارش خدمات دیجیتال
- مدیریت کاربران و سفارش‌ها
- ارتباط خودکار با ادمین‌های هر سرویس
- پنل مدیریت کامل
- سیستم دو زبانه (انگلیسی/فارسی)

</div>

- Service order registration
- User and order management
- Automatic communication with service admins
- Complete admin panel
- Bilingual system (English/Persian)

---

## ✨ Features / ویژگی‌ها

### 🌐 Multilingual / چندزبانه

<div dir="rtl" align="right">

- پشتیبانی کامل از زبان‌های انگلیسی و فارسی
- تغییر زبان در لحظه توسط کاربر
- ذخیره زبان انتخابی هر کاربر در دیتابیس

</div>

- Full support for English and Persian languages
- Real-time language switching by users
- Saving each user's language preference in database

### 📦 Service Management / مدیریت سرویس‌ها

<div dir="rtl" align="right">

۶ نوع سرویس مختلف:
- طراحی وبسایت
- طراحی ربات تلگرام
- سئو و وردپرس
- طراحی گرافیک
- ادمین شبکه‌های اجتماعی
- توسعه وبسایت

</div>

6 different service types:
- Website Design
- Telegram Bot Design
- SEO & WordPress
- Graphic Design
- Social Media Management
- Website Development

### 👤 User Management / مدیریت کاربران

<div dir="rtl" align="right">

- ثبت خودکار کاربران جدید
- ذخیره اطلاعات کامل کاربر
- محدودیت هوشمند سفارش (یک سفارش در انتظار برای هر کاربر)
- دریافت شماره تلفن

</div>

- Automatic registration of new users
- Complete user information storage
- Smart order limiting (one pending order per user)
- Phone number collection

### 👨‍💼 Admin Panel / پنل ادمین

<div dir="rtl" align="right">

- ادمین مجزا برای هر سرویس
- تکمیل سفارش با یک کلیک
- ارسال پیام همگانی به تمام کاربران
- مشاهده همه/در انتظار سفارش‌ها
- فعال/غیرفعال کردن سفارش‌دهی کاربران

</div>

- Separate admin for each service
- Order completion with one click
- Broadcast messaging to all users
- View all/pending orders
- Enable/disable user ordering

### 📊 Database / دیتابیس

<div dir="rtl" align="right">

- دیتابیس SQLite
- ۳ جدول اصلی: کاربران، سفارش‌های خدمات، محدودیت‌های سفارش کاربر
- ذخیره‌سازی خودکار داده‌ها

</div>

- SQLite database
- 3 main tables: users, service_orders, user_order_limits
- Automatic data persistence

---

## 🎥 Demo / دمو

<div dir="rtl" align="right">

برای مشاهده دموی زنده، ربات زیر را در تلگرام استارت کنید:
[@XenwebBot](https://t.me/XenwebBot)

</div>

To see a live demo, start this bot on Telegram:
[@XenwebBot](https://t.me/XenwebBot)

---

## 📋 Prerequisites / پیش‌نیازها

<div dir="rtl" align="right">

- پایتون ۳.۷ یا بالاتر
- توکن ربات تلگرام (از [@BotFather](https://t.me/botfather))
- آشنایی اولیه با ربات‌های تلگرام

</div>

- Python 3.7 or higher
- Telegram Bot Token (from [@BotFather](https://t.me/botfather))
- Basic knowledge of Telegram bots

### Required Python Packages / پکیج‌های مورد نیاز پایتون

```bash
pyTelegramBotAPI==4.12.0
Note: sqlite3, datetime, and os are built-in Python modules and don't need separate installation.

🚀 Installation / نصب
Step 1: Clone the Repository / مرحله ۱: کلون کردن مخزن
bash
git clone https://github.com/XenwebDeveloper/xenweb-bot.git
cd xenweb-bot
Step 2: Install Dependencies / مرحله ۲: نصب وابستگی‌ها
bash
pip install pyTelegramBotAPI
Step 3: Configure the Bot / مرحله ۳: تنظیم ربات
<div dir="rtl" align="right">
فایل bot.py را باز کنید و بخش تنظیمات را پر کنید:

</div>
Open bot.py and fill in the configuration section:

python
# ================== CONFIGURATION ==================
TOKEN = "YOUR_BOT_TOKEN_HERE"  # Bot Token from @BotFather
ADMIN_USERNAME = "your_username"  # Admin username without @
ADMIN_ID = 123456789  # Your Telegram ID

# Service-specific admins (replace with actual admin IDs)
SERVICE_ADMINS = {
    'website_design': 123456789,  # Website design admin ID
    'telegram_bot': 123456789,     # Telegram bot admin ID
    'seo_wordpress': 123456789,    # SEO/WordPress admin ID
    'graphic_design': 123456789,   # Graphic design admin ID
    'social_media': 123456789,     # Social media admin ID
    'website_development': 123456789  # Website development admin ID
}

# Admin password command
ADMIN_PASSWORD = "/pass"  # You can change this
Step 4: Add Social Media Links / مرحله ۴: افزودن لینک‌های شبکه‌های اجتماعی
<div dir="rtl" align="right">
خط ۶۵۰ را در کد پیدا کنید و لینک‌های خود را اضافه کنید:

</div>
Find line ~650 in the code and add your links:

python
# Line ~650: Communication channels
markup.add(
    types.InlineKeyboardButton("Instagram", url="YOUR_INSTAGRAM_URL"),
    types.InlineKeyboardButton("x.com", url="YOUR_X_URL")
)
markup.add(types.InlineKeyboardButton("Github", url="YOUR_GITHUB_URL"))
Step 5: Run the Bot / مرحله ۵: اجرای ربات
bash
python bot.py
<div dir="rtl" align="right">
اگر همه چیز درست باشد، پیام زیر را می‌بینید:

</div>
If everything is correct, you'll see:

text
The bot is running. To stop the bot, press Ctrl + C.
Service Admins Configuration:
  website_design: Admin ID = 123456789
  telegram_bot: Admin ID = 123456789
  ...
⚙️ Configuration Details / جزئیات تنظیمات
Getting a Bot Token / دریافت توکن ربات
<div dir="rtl" align="right">
تلگرام را باز کنید و @BotFather را جستجو کنید

دستور /newbot را ارسال کنید

نام و یوزرنیم ربات را انتخاب کنید

توکن ارائه شده را کپی کنید

</div>
Open Telegram and search for @BotFather

Send /newbot command

Choose a name and username for your bot

Copy the token provided

Finding Your Telegram ID / پیدا کردن آیدی تلگرام
<div dir="rtl" align="right">
@userinfobot را در تلگرام جستجو کنید

دستور /start را ارسال کنید

آیدی عددی خود را در پیام دریافتی پیدا کنید

</div>
Search for @userinfobot on Telegram

Send /start command

Find your numeric ID in the received message

Admin Structure / ساختار ادمین‌ها
<div dir="rtl" align="right">
ادمین اصلی: به تمام امکانات دسترسی دارد و گزارش خطاها را دریافت می‌کند

ادمین‌های سرویس: فقط نوتیفیکیشن‌های سرویس خاص خود را دریافت می‌کنند

</div>
Main Admin: Has access to all features and receives error reports

Service Admins: Receive notifications only for their specific services

📁 Project Structure / ساختار پروژه
text
xenweb-bot/
│
├── bot.py                 # Main bot file / فایل اصلی ربات
├── users.db               # SQLite database (auto-created) / دیتابیس (ایجاد خودکار)
├── README.md              # This file / این فایل
└── requirements.txt       # Dependencies / وابستگی‌ها
Code Structure / ساختار کد:
text
1. Imports / واردات کتابخانه‌ها
2. Configuration / تنظیمات
3. Database Setup / راه‌اندازی دیتابیس
4. Admin Sessions / نشست‌های ادمین
5. Language Management / مدیریت زبان
6. Bilingual Texts / متون دو زبانه
7. Service Management / مدیریت سرویس‌ها
8. Helper Functions / توابع کمکی
9. Menu System / سیستم منوها
10. Command Handlers / هندلرهای دستورات
11. Admin Panel / پنل ادمین
12. Bot Execution / اجرای ربات
🎯 Usage / نحوه استفاده
For Users / برای کاربران
<div dir="rtl" align="right">
شروع کار با ربات:

دستور /start را ارسال کنید

زبان خود را انتخاب کنید (انگلیسی یا فارسی)

منوی اصلی نمایش داده می‌شود

گزینه‌های منوی اصلی:

خدمات: مشاهده و سفارش خدمات دیجیتال

سفارش‌های من: مشاهده تاریخچه سفارش‌ها

کانال‌های ارتباطی: دسترسی به لینک‌های شبکه‌های اجتماعی

تماس با ادمین: دریافت اطلاعات تماس ادمین

تغییر زبان: تغییر بین انگلیسی/فارسی

</div>
Starting with the bot:

Send /start command

Select your language (English or Persian)

Main menu will be displayed

Main menu options:

Services: View and order digital services

My Orders: Check your order history

Communication channels: Access social media links

Contact admin: Get admin contact info

Change Language: Switch between English/Persian

Ordering a Service / سفارش سرویس
<div dir="rtl" align="right">
روی منوی "خدمات" کلیک کنید

سرویس مورد نظر خود را انتخاب کنید

اگر سفارش در انتظاری نداشته باشید، پیام تایید دریافت می‌کنید

ادمین سرویس به زودی با شما تماس می‌گیرد

</div>
Click on "Services" menu

Select your desired service

If you have no pending orders, you'll receive a confirmation message

The service admin will contact you soon

Contacting Admin / تماس با ادمین
<div dir="rtl" align="right">
روی "تماس با ادمین" کلیک کنید

اگر شماره تلفن خود را به اشتراک نگذاشته باشید، از شما خواسته می‌شود

پس از اشتراک‌گذاری، اطلاعات تماس ادمین را دریافت می‌کنید

ادمین از درخواست شما مطلع می‌شود

</div>
Click on "Contact admin"

If you haven't shared your phone number, you'll be prompted to do so

After sharing, you'll receive admin contact info

The admin gets notified about your request

👨‍💼 Admin Panel / پنل ادمین
Accessing Admin Panel / دسترسی به پنل ادمین
<div dir="rtl" align="right">
رمز عبور ادمین (پیش‌فرض: /pass) را به ربات ارسال کنید

</div>
Send the admin password (default: /pass) to the bot

Admin Menu Options / گزینه‌های منوی ادمین
1. View Pending Orders / مشاهده سفارش‌های در انتظار
<div dir="rtl" align="right">تمام سفارش‌های با وضعیت "در انتظار" را نشان می‌دهد</div> Shows all orders with 'pending' status
2. View All Orders / مشاهده همه سفارش‌ها
<div dir="rtl" align="right">آخرین ۲۰ سفارش را با وضعیت آنها نشان می‌دهد</div> Shows last 20 orders with their status
3. Complete Order / تکمیل سفارش
<div dir="rtl" align="right">شناسه سفارش را وارد کنید تا به عنوان تکمیل شده علامت بخورد</div> Enter order ID to mark as completed
4. Allow New Orders / اجازه سفارش جدید
<div dir="rtl" align="right">شناسه کاربر را وارد کنید تا سفارش‌دهی برای آن کاربر فعال شود</div> Enter user ID to enable ordering for that user
5. Broadcast Message / ارسال پیام همگانی
<div dir="rtl" align="right">ارسال پیام به تمام کاربران</div> Send a message to all users
Order Completion via Inline Button / تکمیل سفارش با دکمه شیشه‌ای
<div dir="rtl" align="right">
وقتی سفارش جدیدی می‌رسد، ادمین‌ها پیامی با موارد زیر دریافت می‌کنند:

دکمه ✅ تکمیل سفارش

دکمه تماس با کاربر (لینک مستقیم)

</div>
When a new order arrives, admins receive a message with:

✅ Complete Order button

Contact User button (direct link)

📊 Database Structure / ساختار دیتابیس
Users Table / جدول کاربران
Column / ستون	Type / نوع	Description / توضیحات
id	INTEGER	Primary key / کلید اصلی
telegram_id	INTEGER	Unique Telegram ID / آیدی یکتای تلگرام
first_name	TEXT	User's first name / نام کاربر
last_name	TEXT	User's last name / نام خانوادگی
username	TEXT	Telegram username / نام کاربری تلگرام
phone	TEXT	Phone number / شماره تلفن
language	TEXT	'en' or 'fa' / 'en' یا 'fa'
created_at	TEXT	Registration date / تاریخ ثبت نام
last_seen	TEXT	Last activity / آخرین فعالیت
Service Orders Table / جدول سفارش‌های خدمات
Column / ستون	Type / نوع	Description / توضیحات
id	INTEGER	Order ID / شناسه سفارش
user_id	INTEGER	User's Telegram ID / آیدی کاربر
username	TEXT	Customer username / نام کاربری مشتری
first_name	TEXT	Customer name / نام مشتری
service_type	TEXT	Internal service code / کد داخلی سرویس
service_name	TEXT	Display service name / نام نمایشی سرویس
admin_id	INTEGER	Responsible admin ID / آیدی ادمین مسئول
status	TEXT	'pending' or 'completed' / 'در انتظار' یا 'تکمیل شده'
order_date	TEXT	Order date / تاریخ سفارش
completed_date	TEXT	Completion date / تاریخ تکمیل
User Order Limits Table / جدول محدودیت‌های سفارش کاربر
Column / ستون	Type / نوع	Description / توضیحات
id	INTEGER	Primary key / کلید اصلی
user_id	INTEGER	User's Telegram ID / آیدی کاربر
pending_orders	INTEGER	Number of pending orders / تعداد سفارش‌های در انتظار
can_order	INTEGER	1 if can order, 0 if blocked / ۱ اگر می‌تواند سفارش دهد، ۰ اگر مسدود شده
last_order_time	TEXT	Last order time / آخرین زمان سفارش
🔧 API Reference / مرجع توابع
Language Management / مدیریت زبان
python
get_user_language(user_id)      # Get user's language / دریافت زبان کاربر
update_user_language(user_id, lang)  # Update user's language / به‌روزرسانی زبان کاربر
get_text(key, user_id, **kwargs)  # Get translated text / دریافت متن ترجمه شده
Order Management / مدیریت سفارش
python
check_user_can_order(user_id)    # Check if user can order / بررسی امکان سفارش کاربر
create_service_order(user_id, first_name, username, service_type, service_name)  # Create new order / ایجاد سفارش جدید
complete_order(order_id)          # Complete an order / تکمیل سفارش
get_user_orders(user_id, status_filter=None, limit=20)  # Get user orders / دریافت سفارش‌های کاربر
Database Operations / عملیات دیتابیس
python
save_or_update_user(user)         # Save or update user / ذخیره یا به‌روزرسانی کاربر
save_phone_number(user_id, phone)  # Save phone number / ذخیره شماره تلفن
has_phone_number(user_id)          # Check if user has phone / بررسی وجود شماره تلفن
🔍 Troubleshooting / عیب‌یابی
Common Issues / مشکلات رایج
1. Bot Doesn't Start / ربات اجرا نمی‌شود
<div dir="rtl" align="right">
مشکل: بعد از اجرای python bot.py هیچ پیامی نمایش داده نمی‌شود یا خطا می‌دهد.

راه‌حل:

مطمئن شوید توکن ربات درست وارد شده است

بررسی کنید پایتون ۳.۷ یا بالاتر نصب باشد

کتابخانه pyTelegramBotAPI را نصب کنید: pip install pyTelegramBotAPI

</div>
Problem: After running python bot.py, no message appears or error occurs.

Solution:

Make sure the bot token is correctly entered

Check that Python 3.7+ is installed

Install pyTelegramBotAPI: pip install pyTelegramBotAPI

2. Admins Don't Receive Notifications / ادمین‌ها نوتیفیکیشن دریافت نمی‌کنند
<div dir="rtl" align="right">
مشکل: وقتی کاربر سفارش می‌دهد، ادمین پیامی دریافت نمی‌کند.

راه‌حل:

بررسی کنید آیدی ادمین‌ها درست وارد شده باشد

مطمئن شوید ادمین ربات را استارت کرده باشد (/start)

بررسی کنید ادمین ربات را بلاک نکرده باشد

</div>
Problem: When a user orders, the admin doesn't receive a message.

Solution:

Check that admin IDs are correctly entered

Make sure the admin has started the bot (/start)

Check that the admin hasn't blocked the bot

3. Database Errors / خطاهای دیتابیس
<div dir="rtl" align="right">
مشکل: خطاهای مربوط به دیتابیس ظاهر می‌شود.

راه‌حل:

فایل users.db را حذف کنید (دیتابیس دوباره ساخته می‌شود)

مطمئن شوید پایتون مجوز نوشتن در پوشه فعلی را دارد

</div>
Problem: Database-related errors appear.

Solution:

Delete the users.db file (it will be recreated)

Make sure Python has write permissions in the current directory

🤝 Contributing / مشارکت
<div dir="rtl" align="right">
مشارکت‌ها پذیرفته می‌شوند! لطفاً مراحل زیر را دنبال کنید:

مخزن را Fork کنید

یک Branch جدید ایجاد کنید (git checkout -b feature/improvement)

تغییرات خود را Commit کنید (git commit -am 'Add new feature')

به Branch خود Push کنید (git push origin feature/improvement)

یک Pull Request ایجاد کنید

</div>
Contributions are welcome! Please follow these steps:

Fork the repository

Create a new branch (git checkout -b feature/improvement)

Commit your changes (git commit -am 'Add new feature')

Push to the branch (git push origin feature/improvement)

Create a Pull Request

Development Guidelines / راهنمای توسعه
<div dir="rtl" align="right">
ساختار دو زبانه را حفظ کنید

برای منطق پیچیده کامنت اضافه کنید

هنگام افزودن ویژگی‌ها، مستندات را به‌روز کنید

</div>
Keep the bilingual structure

Add comments for complex logic

Update documentation when adding features

📄 License / لیسانس
<div dir="rtl" align="right">
این پروژه تحت لیسانس MIT منتشر شده است - برای جزئیات بیشتر فایل LICENSE را مشاهده کنید.

</div>
This project is licensed under the MIT License - see the LICENSE file for details.

text
MIT License

Copyright (c) 2024 XenwebDeveloper

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files...
📞 Contact / تماس
<div dir="rtl" align="right">
توسعه‌دهنده: XenwebDeveloper

گیت‌هاب: https://github.com/XenwebDeveloper

تلگرام: @XenwebDeveloper

ایمیل: xenweb.developer@gmail.com

برای پشتیبانی، یک Issue در گیت‌هاب باز کنید یا از طریق تلگرام تماس بگیرید.

</div>
Developer: XenwebDeveloper

GitHub: https://github.com/XenwebDeveloper

Telegram: @XenwebDeveloper

Email: xenweb.developer@gmail.com

For support, open an issue on GitHub or contact via Telegram.

🌟 Support / حمایت
<div dir="rtl" align="right">
اگر این پروژه برای شما مفید بود، لطفاً به آن ستاره ⭐ بدهید!

</div>
If you found this project helpful, please give it a star ⭐!

<div align="center">
Made with ❤️ for the Telegram community
ساخته شده با ❤️ برای جامعه تلگرام

© 2024 XenwebDeveloper - All Rights Reserved

</div> ```
