import telebot
from telebot import types
import sqlite3
from datetime import datetime
import os

# ================== CONFIGURATION ==================
TOKEN = ""  # Bot Token
ADMIN_USERNAME = ""  # Admin username without @
ADMIN_ID = 1111111111  # Your Telegram ID

# Service-specific admins (customize these IDs)
SERVICE_ADMINS = {
    # Website design admin ID
    'website_design': 1,
    # Telegram bot admin ID 
    'telegram_bot': 1,
    # SEO/WordPress admin ID
    'seo_wordpress': 1,
    # Graphic design admin ID
    'graphic_design': 1,
    # Social media admin ID
    'social_media': 1,
    # Website development admin ID
    'website_development': 1
}

# Admin password command
ADMIN_PASSWORD = "/pass"

# Initialize bot
bot = telebot.TeleBot(TOKEN)

# ================== DATABASE SETUP ==================
# Initialize database connection
conn = sqlite3.connect("users.db", check_same_thread=False)
cursor = conn.cursor()

# Create tables if not exist
cursor.execute("""
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    telegram_id INTEGER UNIQUE,
    first_name TEXT,
    last_name TEXT,
    username TEXT,
    phone TEXT,
    language TEXT DEFAULT 'en',
    created_at TEXT,
    last_seen TEXT
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS service_orders (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER,
    username TEXT,
    first_name TEXT,
    service_type TEXT,
    service_name TEXT,
    admin_id INTEGER,
    status TEXT DEFAULT 'pending',
    order_date TEXT,
    completed_date TEXT,
    FOREIGN KEY (user_id) REFERENCES users(telegram_id)
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS user_order_limits (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER UNIQUE,
    pending_orders INTEGER DEFAULT 0,
    can_order INTEGER DEFAULT 1,
    last_order_time TEXT,
    FOREIGN KEY (user_id) REFERENCES users(telegram_id)
)
""")

conn.commit()

# ================== ADMIN SESSIONS ==================
admin_sessions = set()

# ================== LANGUAGE MANAGEMENT ==================
LANGUAGES = {
    'en': 'English 🇺🇸',
    'fa': 'فارسی 🇮🇷'
}

USER_LANGUAGES = {}

def get_user_language(user_id):
    """Get user language from database or cache."""
    if user_id in USER_LANGUAGES:
        return USER_LANGUAGES[user_id]
    
    cursor.execute("SELECT language FROM users WHERE telegram_id=?", (user_id,))
    result = cursor.fetchone()
    
    if result and result[0]:
        lang = result[0]
    else:
        lang = 'en'
    
    USER_LANGUAGES[user_id] = lang
    return lang

def update_user_language(user_id, lang):
    """Update user language in database and cache."""
    cursor.execute("UPDATE users SET language=? WHERE telegram_id=?", (lang, user_id))
    conn.commit()
    USER_LANGUAGES[user_id] = lang

# ================== BILINGUAL TEXTS ==================
TEXTS = {
    'en': {
        'welcome': "Welcome to the Xenweb BOT👋\nYou can change the language from the menu below",
        'menu_services': "Services 🛠",
        'menu_my_orders': "My Orders 📋",
        'menu_channels': "Communication channels 🌐",
        'menu_admin': "Contact the admin 📞",
        'menu_language': "Change Language 🌐",
        #=====================================
        'services_title': "Select a service:",
        'website_design': "Website Design",
        'telegram_bot': "Telegram Bot",
        'seo_wordpress': "SEO & WordPress",
        'graphic_design': "Graphic Design",
        'social_media': "Social Media Admin",
        'website_development': "Website Development",
        #=====================================
        'order_confirmed': "Your ticket was registered for ({service}) ✅\n\nThe admin will contact you shortly.\n⚠️ Please do not submit another request.",
        'pending_order_exists': "You already have a pending ticket ⏳\nPlease wait for the admin to contact you.",
        'order_limit_reached': "You have reached the ticket limit ❌\nPlease wait for your previous orders to be completed.",
        'contact_admin_prompt': "To get the admin contact information, please share your phone number:\n\nClick the button below 👇",
        'share_number_button': "Share Phone Number",
        'number_saved': "Thank you!✅\nAdmin: @{admin_username}\nYou can contact the admin directly.",
        'number_already_saved': "Admin: @{admin_username}\nYou can contact the admin directly.",
        'admin_will_contact': "The admin will contact you shortly.",
        #=====================================
        'channels_title': "Ways of communication 👇",
        'select_language': "Please select your language:",
        'language_changed': "Language changed to {language} ✅",
        #=====================================
        'new_order_notification': "NEW ORDER RECEIVED\n\nService: {service}\nCustomer: {first_name}\nUsername: @{username}\nPhone: {phone}\nUser ID: {customer_id}\nOrder Time: {time}\n\nPlease contact the customer as soon as possible.",
        'admin_contact_notification': "CONTACT REQUEST\n\nUser: {first_name}\nUsername: @{username}\nPhone: {phone}\nUser ID: {customer_id}\nTime: {time}\n\nUser wants to contact you.",
        #=====================================
        'order_completed': "Order #{order_id} has been completed ✅",
        'no_pending_orders': "No pending orders ✅",
        'order_already_completed': "This order is already completed ⚠️",
        #=====================================
        'admin_panel': "==== ADMIN PANEL ====\n\nSelect an option:",
        'view_pending_orders': "View Pending Orders",
        'view_all_orders': "View All Orders",
        'complete_order': "Complete Order",
        'allow_new_orders': "Allow New Orders",
        'broadcast_message': "Broadcast Message",
        'my_orders_title': "Your Orders\n\nSelect an option:",
        'view_active_orders': "Active Orders",
        'view_completed_orders': "Completed Orders",
        'view_all_my_orders': "All My Orders",
        'active_orders_title': "Your Active Orders:\n\n",
        'completed_orders_title': "Your Completed Orders:\n\n",
        'all_orders_title': "All Your Orders:\n\n",
        'no_orders_found': "No orders found.",
        #=====================================
        'order_details': "Order #{order_id}\n📋 {service}\n📅 Ordered: {order_date}\n{status_icon} Status: {status}\n{completed_info}",
        'order_status_pending': "pending ⏳",
        'order_status_completed': "completed ✅",
        'completed_on': "Completed on: {completed_date}",
        'phone_required': "Phone number is required to contact admin.",
        'phone_shared_success': "Phone number shared successfully! ✅",
        'contact_admin_info': "Admin: @{admin_username}\n📱 You can now contact the admin directly."
    },
    'fa': {
        'welcome': "به ربات XENWEB خوش آمدید👋\nاز منوی زیر برای خدمات استفاده کنید.",
        'menu_services': "خدمات 🛠",
        'menu_my_orders': "سفارش‌های من 📋",
        'menu_channels': "کانال های ارتباطی 🌐",
        'menu_admin': "تماس با ادمین 📞",
        'menu_language': "تغییر زبان 🌐",
        #=====================================
        'services_title': "یک سرویس را انتخاب کنید:",
        'website_design': "طراحی وبسایت",
        'telegram_bot': "طراحی ربات تلگرام",
        'seo_wordpress': "سئو و وردپرس",
        'graphic_design': "طراحی گرافیک",
        'social_media': "ادمین شبکه‌های اجتماعی",
        'website_development': "توسعه وبسایت",
        #=====================================
        'order_confirmed': "✅ سفارش شما برای ({service}) ثبت شد.\n\nادمین به زودی با شما تماس خواهد گرفت.\n\n⚠️ لطفاً درخواست دیگری ارسال نکنید.",
        'pending_order_exists': "⏳ شما قبلاً یک سفارش در انتظار دارید.\nلطفاً منتظر تماس ادمین باشید.",
        'order_limit_reached': "❌ شما به محدودیت سفارش رسیده‌اید.\nلطفاً منتظر تکمیل سفارش‌های قبلی باشید.",
        'contact_admin_prompt': "برای دریافت اطلاعات تماس ادمین، لطفاً شماره تلفن خود را به اشتراک بگذارید:\n\n👇 دکمه زیر را فشار دهید",
        'share_number_button': "📱 اشتراک‌گذاری شماره تلفن",
        'number_saved': "✅ متشکرم! شماره تلفن شما ذخیره شد.\n\n👤 ادمین: @{admin_username}\n📱 اکنون می‌توانید با ادمین تماس بگیرید.",
        'number_already_saved': "✅ شماره تلفن شما قبلاً ذخیره شده است.\n\n👤 ادمین: @{admin_username}\n📱 اکنون می‌توانید با ادمین تماس بگیرید.",
        'admin_will_contact': "ادمین به زودی با شما تماس خواهد گرفت.",
        #=====================================
        'channels_title': "راه‌های ارتباطی 👇",
        'select_language': "لطفاً زبان خود را انتخاب کنید:",
        'language_changed': "زبان به {language} تغییر کرد ✅",
        #=====================================
        'new_order_notification': "🆕 سفارش جدید دریافت شد\n\n📋 سرویس: {service}\n👤 مشتری: {first_name}\n📱 یوزرنیم: @{username}\n📞 شماره: {phone}\n🆔 آی‌دی کاربر: {customer_id}\n⏰ زمان سفارش: {time}\n\nلطفاً در اسرع وقت با مشتری تماس بگیرید.",
        'admin_contact_notification': "📞 درخواست تماس\n\n👤 کاربر: {first_name}\n📱 یوزرنیم: @{username}\n📞 شماره: {phone}\n🆔 آی‌دی کاربر: {customer_id}\n⏰ زمان: {time}\n\nکاربر می‌خواهد با شما تماس بگیرد.",
        #=====================================
        'order_completed': "✅ سفارش شماره #{order_id} تکمیل شد.",
        'no_pending_orders': "✅ هیچ سفارش در انتظاری وجود ندارد.",
        'order_already_completed': "⚠️ این سفارش قبلاً تکمیل شده است.",
        #=====================================
        'admin_panel': "==== پنل ادمین ====\n\nیک گزینه را انتخاب کنید:",
        'view_pending_orders': "مشاهده سفارش‌های در انتظار",
        'view_all_orders': "مشاهده تمام سفارش‌ها",
        'complete_order': "تکمیل سفارش",
        'allow_new_orders': "اجازه سفارش جدید",
        'broadcast_message': "ارسال پیام همگانی",
        'my_orders_title': "سفارش‌های شما\n\nیک گزینه را انتخاب کنید:",
        'view_active_orders': "سفارش‌های فعال",
        'view_completed_orders': "سفارش‌های تکمیل شده",
        'view_all_my_orders': "تمام سفارش‌های من",
        'active_orders_title': "سفارش‌های فعال شما:\n\n",
        'completed_orders_title': "سفارش‌های تکمیل شده شما:\n\n",
        'all_orders_title': "تمام سفارش‌های شما:\n\n",
        'no_orders_found': "سفارشی یافت نشد.",
        #=====================================
        'order_details': "🆔 سفارش #{order_id}\n📋 {service}\n📅 تاریخ سفارش: {order_date}\n{status_icon} وضعیت: {status}\n{completed_info}",
        'order_status_pending': "در انتظار ⏳",
        'order_status_completed': "تکمیل شده ✅",
        'completed_on': "✅ تکمیل شده در: {completed_date}",
        'phone_required': "📞 برای تماس با ادمین نیاز به شماره تلفن دارید.",
        'phone_shared_success': "✅ شماره تلفن با موفقیت به اشتراک گذاشته شد!",
        'contact_admin_info': "👤 ادمین: @{admin_username}\n📱 اکنون می‌توانید با ادمین تماس بگیرید."
    }
}

def get_text(key, user_id, **kwargs):
    """Get translated text based on user's language."""
    lang = get_user_language(user_id)
    text = TEXTS[lang].get(key, key)
    return text.format(**kwargs) if kwargs else text

# ================== SERVICE ORDER MANAGEMENT ==================
def check_user_can_order(user_id):
    """Check if user can place a new order."""
    cursor.execute("SELECT can_order, pending_orders FROM user_order_limits WHERE user_id=?", (user_id,))
    result = cursor.fetchone()
    
    if not result:
        cursor.execute("INSERT INTO user_order_limits (user_id, can_order, pending_orders, last_order_time) VALUES (?, 1, 0, ?)", 
                      (user_id, get_current_time()))
        conn.commit()
        return True
    
    can_order, pending_orders = result
    
    return can_order == 1 and pending_orders == 0

def create_service_order(user_id, first_name, username, service_type, service_name):
    """Create a new service order."""
    current_time = get_current_time()
    admin_id = SERVICE_ADMINS.get(service_type, ADMIN_ID)
    
    cursor.execute("SELECT phone FROM users WHERE telegram_id=?", (user_id,))
    phone_result = cursor.fetchone()
    phone = phone_result[0] if phone_result and phone_result[0] else "Not provided"
    
    cursor.execute("""
    INSERT INTO service_orders (user_id, username, first_name, service_type, service_name, admin_id, order_date, status)
    VALUES (?, ?, ?, ?, ?, ?, ?, 'pending')
    """, (user_id, username, first_name, service_type, service_name, admin_id, current_time))
    
    order_id = cursor.lastrowid
    
    cursor.execute("""
    INSERT OR REPLACE INTO user_order_limits (user_id, can_order, pending_orders, last_order_time)
    VALUES (?, 1, COALESCE((SELECT pending_orders FROM user_order_limits WHERE user_id=?), 0) + 1, ?)
    """, (user_id, user_id, current_time))
    
    conn.commit()
    
    notify_service_admin(order_id, user_id, first_name, username, phone, service_name, admin_id, current_time)
    
    return order_id

def notify_service_admin(order_id, user_id, first_name, username, phone, service_name, admin_id, time):
    """Notify service admin about new order."""
    message = get_text('new_order_notification', admin_id,
                      service=service_name,
                      first_name=first_name,
                      username=username,
                      phone=phone,
                      customer_id=user_id,
                      time=time)
    
    markup = types.InlineKeyboardMarkup()
    markup.row(
        types.InlineKeyboardButton("✅ Complete Order", callback_data=f"complete_{order_id}"),
        types.InlineKeyboardButton("Contact User", url=f"https://t.me/{username}" if username != "no_username" else f"tg://user?id={user_id}")
    )
    
    try:
        bot.send_message(admin_id, message, reply_markup=markup)
    except Exception as e:
        print(f"Error sending to admin {admin_id}: {e}")
        if admin_id != ADMIN_ID:
            bot.send_message(ADMIN_ID, f"Failed to send to service admin. Order details:\n{message}", reply_markup=markup)

def notify_admin_contact_request(user_id, first_name, username, phone, time):
    """Notify admin about contact request."""
    # Use customer_id instead of user_id
    message = get_text('admin_contact_notification', ADMIN_ID,
                      first_name=first_name,
                      username=username,
                      phone=phone,
                      customer_id=user_id,
                      time=time)
    
    try:
        bot.send_message(ADMIN_ID, message)
    except Exception as e:
        print(f"Error sending contact notification to admin: {e}")

def complete_order(order_id):
    """Mark an order as completed."""
    cursor.execute("SELECT user_id, status FROM service_orders WHERE id=?", (order_id,))
    result = cursor.fetchone()
    
    if not result:
        return False, "Order not found"
    
    user_id, status = result
    
    if status == 'completed':
        return False, "already_completed"
    
    current_time = get_current_time()
    
    cursor.execute("UPDATE service_orders SET status='completed', completed_date=? WHERE id=?", 
                  (current_time, order_id))
    cursor.execute("UPDATE user_order_limits SET pending_orders = pending_orders - 1 WHERE user_id=? AND pending_orders > 0", 
                  (user_id,))
    conn.commit()
    
    return True, "success"

def get_service_display_name(service_type, user_id):
    """Get display name for service based on language."""
    lang = get_user_language(user_id)
    service_names = {
        'website_design': get_text('website_design', user_id),
        'telegram_bot': get_text('telegram_bot', user_id),
        'seo_wordpress': get_text('seo_wordpress', user_id),
        'graphic_design': get_text('graphic_design', user_id),
        'social_media': get_text('social_media', user_id),
        'website_development': get_text('website_development', user_id)
    }
    return service_names.get(service_type, service_type)

def get_user_orders(user_id, status_filter=None, limit=20):
    """Get user's orders with optional status filter."""
    query = "SELECT id, service_name, status, order_date, completed_date FROM service_orders WHERE user_id=?"
    params = [user_id]
    
    if status_filter:
        query += " AND status=? "
        params.append(status_filter)
    
    query += " ORDER BY order_date DESC "
    
    if limit:
        query += " LIMIT ? "
        params.append(limit)
    
    cursor.execute(query, tuple(params))
    return cursor.fetchall()

def format_order_for_display(order, user_id):
    """Format order details for display."""
    order_id, service_name, status, order_date, completed_date = order
    
    status_icon = "⏳" if status == 'pending' else "✅"
    status_text = get_text('order_status_pending', user_id) if status == 'pending' else get_text('order_status_completed', user_id)
    
    completed_info = ""
    if status == 'completed' and completed_date:
        completed_info = get_text('completed_on', user_id, completed_date=completed_date)
    
    return get_text('order_details', user_id,
                   order_id=order_id,
                   service=service_name,
                   order_date=order_date,
                   status_icon=status_icon,
                   status=status_text,
                   completed_info=completed_info)

def has_phone_number(user_id):
    """Check if user has provided phone number."""
    cursor.execute("SELECT phone FROM users WHERE telegram_id=?", (user_id,))
    result = cursor.fetchone()
    
    return result and result[0] and result[0].strip() != ""

def save_phone_number(user_id, phone_number):
    """Save user's phone number to database."""
    cursor.execute("UPDATE users SET phone=? WHERE telegram_id=?", (phone_number, user_id))
    conn.commit()

# ================== HELPER FUNCTIONS ==================
def get_current_time():
    """Get current timestamp as formatted string."""
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

def save_or_update_user(user):
    """Save new user or update existing user's information."""
    cursor.execute("""
    INSERT INTO users (telegram_id, first_name, last_name, username, created_at, last_seen, language, phone)
    VALUES (?, ?, ?, ?, ?, ?, ?, ?)
    ON CONFLICT(telegram_id) DO UPDATE SET
        first_name=excluded.first_name,
        last_name=excluded.last_name,
        username=excluded.username,
        last_seen=excluded.last_seen
    """, (
        user.id,
        user.first_name,
        user.last_name,
        user.username,
        get_current_time(),
        get_current_time(),
        'en',
        ''
    ))
    conn.commit()
    USER_LANGUAGES[user.id] = 'en'

# ================== MENU SYSTEM ==================
def create_main_menu(user_id):
    """Create main menu based on user's language."""
    lang = get_user_language(user_id)
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    
    if lang == 'fa':
        btn_services = types.KeyboardButton(get_text('menu_services', user_id))
        btn_my_orders = types.KeyboardButton(get_text('menu_my_orders', user_id))
        btn_channels = types.KeyboardButton(get_text('menu_channels', user_id))
        btn_admin = types.KeyboardButton(get_text('menu_admin', user_id))
        btn_language = types.KeyboardButton(get_text('menu_language', user_id))
        
        markup.row(btn_services)
        markup.row(btn_my_orders, btn_channels)
        markup.row(btn_admin, btn_language)
    else:
        btn_services = types.KeyboardButton(get_text('menu_services', user_id))
        btn_my_orders = types.KeyboardButton(get_text('menu_my_orders', user_id))
        btn_channels = types.KeyboardButton(get_text('menu_channels', user_id))
        btn_admin = types.KeyboardButton(get_text('menu_admin', user_id))
        btn_language = types.KeyboardButton(get_text('menu_language', user_id))
        
        markup.row(btn_services)
        markup.row(btn_my_orders, btn_channels)
        markup.row(btn_admin, btn_language)
    
    return markup

def create_services_menu(user_id):
    """Create services selection menu."""
    markup = types.InlineKeyboardMarkup(row_width=2)
    markup.add(
        types.InlineKeyboardButton(get_text('website_design', user_id), callback_data="service_website_design"),
        types.InlineKeyboardButton(get_text('telegram_bot', user_id), callback_data="service_telegram_bot"),
        types.InlineKeyboardButton(get_text('seo_wordpress', user_id), callback_data="service_seo_wordpress"),
        types.InlineKeyboardButton(get_text('graphic_design', user_id), callback_data="service_graphic_design"),
        types.InlineKeyboardButton(get_text('social_media', user_id), callback_data="service_social_media"),
        types.InlineKeyboardButton(get_text('website_development', user_id), callback_data="service_website_development")
    )
    return markup

def create_my_orders_menu(user_id):
    """Create 'My Orders' menu."""
    markup = types.InlineKeyboardMarkup(row_width=2)
    markup.add(
        types.InlineKeyboardButton(get_text('view_active_orders', user_id), callback_data="myorders_active"),
        types.InlineKeyboardButton(get_text('view_completed_orders', user_id), callback_data="myorders_completed"),
        types.InlineKeyboardButton(get_text('view_all_my_orders', user_id), callback_data="myorders_all")
    )
    return markup

def ask_user_language(message):
    """Ask user to select preferred language."""
    markup = types.InlineKeyboardMarkup()
    markup.add(
        types.InlineKeyboardButton("English 🇺🇸", callback_data="setlang_en"),
        types.InlineKeyboardButton("فارسی 🇮🇷", callback_data="setlang_fa")
    )
    bot.send_message(
        message.chat.id,
        "Please select your language / لطفاً زبان خود را انتخاب کنید:",
        reply_markup=markup
    )

def ask_for_phone_number(user_id, chat_id):
    """Ask user to share phone number."""
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    markup.add(types.KeyboardButton(
        get_text('share_number_button', user_id),
        request_contact=True
    ))
    bot.send_message(
        chat_id,
        get_text('contact_admin_prompt', user_id),
        reply_markup=markup
    )

# ================== COMMAND HANDLERS ==================
@bot.message_handler(commands=["start"])
def handle_start(message):
    """Handle /start command for new and existing users."""
    user = message.from_user
    user_id = user.id
    
    cursor.execute("SELECT telegram_id FROM users WHERE telegram_id=?", (user_id,))
    user_exists = cursor.fetchone()
    
    if not user_exists:
        save_or_update_user(user)
        ask_user_language(message)
    else:
        cursor.execute("UPDATE users SET first_name=?, last_name=?, username=?, last_seen=? WHERE telegram_id=?", 
                      (user.first_name, user.last_name, user.username, get_current_time(), user_id))
        conn.commit()
        
        cursor.execute("SELECT language FROM users WHERE telegram_id=?", (user_id,))
        result = cursor.fetchone()
        
        if result and result[0]:
            lang = result[0]
            USER_LANGUAGES[user_id] = lang
            bot.send_message(
                message.chat.id,
                get_text('welcome', user_id),
                reply_markup=create_main_menu(user_id)
            )
        else:
            ask_user_language(message)

@bot.callback_query_handler(func=lambda call: call.data.startswith("setlang_"))
def handle_language_selection(call):
    """Handle language selection from inline keyboard."""
    user_id = call.from_user.id
    lang = call.data.split("_")[1]
    
    update_user_language(user_id, lang)
    
    try:
        bot.delete_message(call.message.chat.id, call.message.message_id)
    except:
        pass
    
    lang_name = "English" if lang == 'en' else "فارسی"
    bot.send_message(
        call.message.chat.id,
        get_text('language_changed', user_id, language=lang_name),
        reply_markup=create_main_menu(user_id)
    )

@bot.message_handler(func=lambda m: m.text in ["Change Language 🌐", "تغییر زبان 🌐"])
def handle_change_language(message):
    """Handle change language request from menu."""
    ask_user_language(message)

# ================== SERVICES HANDLER ==================
@bot.message_handler(func=lambda m: m.text in ["Services 🛠", "خدمات 🛠"])
def handle_services(message):
    """Display services selection menu."""
    user_id = message.from_user.id
    bot.send_message(
        message.chat.id,
        get_text('services_title', user_id),
        reply_markup=create_services_menu(user_id)
    )

@bot.callback_query_handler(func=lambda call: call.data.startswith("service_"))
def handle_service_selection(call):
    """Handle service selection from user."""
    user_id = call.from_user.id
    first_name = call.from_user.first_name
    username = call.from_user.username or "no_username"
    service_type = call.data.replace("service_", "")
    
    if not check_user_can_order(user_id):
        cursor.execute("SELECT pending_orders FROM user_order_limits WHERE user_id=?", (user_id,))
        result = cursor.fetchone()
        
        if result and result[0] > 0:
            bot.answer_callback_query(call.id, get_text('pending_order_exists', user_id))
            bot.send_message(call.message.chat.id, get_text('pending_order_exists', user_id))
        else:
            bot.answer_callback_query(call.id, get_text('order_limit_reached', user_id))
            bot.send_message(call.message.chat.id, get_text('order_limit_reached', user_id))
        return
    
    service_name = get_service_display_name(service_type, user_id)
    order_id = create_service_order(user_id, first_name, username, service_type, service_name)
    
    bot.answer_callback_query(call.id, "✅ Order submitted")
    bot.send_message(
        call.message.chat.id,
        get_text('order_confirmed', user_id, service=service_name)
    )

# ================== CONTACT ADMIN HANDLER ==================
@bot.message_handler(func=lambda m: m.text in ["Contact the admin 📞", "تماس با ادمین 📞"])
def handle_contact_admin(message):
    """Handle admin contact request."""
    user_id = message.from_user.id
    
    if has_phone_number(user_id):
        # If user already has phone number, show admin info immediately
        bot.send_message(
            message.chat.id,
            get_text('number_already_saved', user_id, admin_username=ADMIN_USERNAME)
        )
    else:
        # Ask for phone number and set flag
        waiting_for_admin_contact.add(user_id)
        ask_for_phone_number(user_id, message.chat.id)

# ================== PHONE NUMBER HANDLER ==================
@bot.message_handler(content_types=['contact'])
def handle_contact(message):
    """Handle phone number sharing."""
    user_id = message.from_user.id
    
    if not message.contact:
        return
    
    phone_number = message.contact.phone_number
    save_phone_number(user_id, phone_number)
    
    # Always show admin info after sharing phone number
    if user_id in waiting_for_admin_contact:
        waiting_for_admin_contact.remove(user_id)
        
        # Notify admin about contact request
        first_name = message.from_user.first_name
        username = message.from_user.username or "no_username"
        current_time = get_current_time()
        
        notify_admin_contact_request(user_id, first_name, username, phone_number, current_time)
    
    # Show admin information to user
    bot.send_message(
        message.chat.id,
        get_text('number_saved', user_id, admin_username=ADMIN_USERNAME),
        reply_markup=create_main_menu(user_id)
    )

# ================== MY ORDERS HANDLER ==================
@bot.message_handler(func=lambda m: m.text in ["My Orders 📋", "سفارش‌های من 📋"])
def handle_my_orders(message):
    """Display user's orders menu."""
    user_id = message.from_user.id
    bot.send_message(
        message.chat.id,
        get_text('my_orders_title', user_id),
        reply_markup=create_my_orders_menu(user_id)
    )

@bot.callback_query_handler(func=lambda call: call.data.startswith("myorders_"))
def handle_my_orders_selection(call):
    """Handle my orders menu selection."""
    user_id = call.from_user.id
    order_type = call.data.replace("myorders_", "")
    
    if order_type == 'active':
        orders = get_user_orders(user_id, status_filter='pending')
        title = get_text('active_orders_title', user_id)
    elif order_type == 'completed':
        orders = get_user_orders(user_id, status_filter='completed')
        title = get_text('completed_orders_title', user_id)
    else:
        orders = get_user_orders(user_id)
        title = get_text('all_orders_title', user_id)
    
    if not orders:
        bot.answer_callback_query(call.id, get_text('no_orders_found', user_id))
        bot.send_message(call.message.chat.id, get_text('no_orders_found', user_id))
        return
    
    message_text = title
    for order in orders:
        message_text += format_order_for_display(order, user_id)
        message_text += "\n" + "─" * 30 + "\n"
    
    bot.answer_callback_query(call.id, f"Found {len(orders)} orders")
    bot.send_message(call.message.chat.id, message_text)

# ================== ADMIN CALLBACK HANDLERS ==================
@bot.callback_query_handler(func=lambda call: call.data.startswith("complete_"))
def handle_complete_order(call):
    """Handle order completion by admin."""
    try:
        order_id = int(call.data.replace("complete_", ""))
        success, message = complete_order(order_id)
        
        if success:
            bot.answer_callback_query(call.id, get_text('order_completed', call.from_user.id, order_id=order_id))
            try:
                bot.edit_message_reply_markup(
                    chat_id=call.message.chat.id,
                    message_id=call.message.message_id,
                    reply_markup=None
                )
            except:
                pass
            bot.send_message(call.message.chat.id, get_text('order_completed', call.from_user.id, order_id=order_id))
        elif message == "already_completed":
            bot.answer_callback_query(call.id, get_text('order_already_completed', call.from_user.id))
        else:
            bot.answer_callback_query(call.id, "❌ Order not found")
    except ValueError:
        bot.answer_callback_query(call.id, "❌ Invalid order ID")

@bot.callback_query_handler(func=lambda call: call.data == "admin_pending")
def handle_admin_pending_orders(call):
    """Show pending orders to admin."""
    cursor.execute("SELECT id, first_name, username, service_name, order_date FROM service_orders WHERE status = 'pending' ORDER BY order_date DESC")
    pending_orders = cursor.fetchall()
    
    if not pending_orders:
        bot.answer_callback_query(call.id, get_text('no_pending_orders', call.from_user.id))
        bot.send_message(call.message.chat.id, get_text('no_pending_orders', call.from_user.id))
        return
    
    message = "📋 Pending Orders:\n\n"
    for order in pending_orders:
        message += f"Order #{order[0]}\n"
        message += f"{order[1]} (@{order[2]})\n"
        message += f"Service: {order[3]}\n"
        message += f"Ordered: {order[4]}\n"
        message += "─" * 30 + "\n"
    
    bot.answer_callback_query(call.id, f"Found {len(pending_orders)} pending orders")
    bot.send_message(call.message.chat.id, message)

# ================== ADMIN PANEL ==================
@bot.message_handler(func=lambda m: m.text == ADMIN_PASSWORD)
def handle_admin_login(message):
    """Authenticate admin and show admin panel."""
    admin_sessions.add(message.from_user.id)
    
    markup = types.InlineKeyboardMarkup(row_width=2)
    markup.add(
        types.InlineKeyboardButton(get_text('view_pending_orders', message.from_user.id), callback_data="admin_pending"),
        types.InlineKeyboardButton(get_text('view_all_orders', message.from_user.id), callback_data="admin_all_orders")
    )
    markup.add(
        types.InlineKeyboardButton(get_text('complete_order', message.from_user.id), callback_data="admin_complete_order"),
        types.InlineKeyboardButton(get_text('allow_new_orders', message.from_user.id), callback_data="admin_allow_orders")
    )
    markup.add(
        types.InlineKeyboardButton(get_text('broadcast_message', message.from_user.id), callback_data="admin_broadcast")
    )
    
    bot.send_message(message.chat.id, get_text('admin_panel', message.from_user.id), reply_markup=markup)

@bot.callback_query_handler(func=lambda call: call.data == "admin_all_orders")
def handle_admin_all_orders(call):
    """Show all orders to admin."""
    cursor.execute("SELECT id, first_name, username, service_name, status, order_date, completed_date FROM service_orders ORDER BY order_date DESC LIMIT 20")
    all_orders = cursor.fetchall()
    
    if not all_orders:
        bot.answer_callback_query(call.id, "No orders found")
        bot.send_message(call.message.chat.id, "No orders found")
        return
    
    message = "📊 Recent Orders (Last 20):\n\n"
    for order in all_orders:
        status_icon = "✅" if order[4] == 'completed' else "⏳"
        message += f"{status_icon} Order #{order[0]}\n"
        message += f"{order[1]} (@{order[2]})\n"
        message += f"{order[3]}\n"
        message += f"Ordered: {order[5]}\n"
        if order[6]:
            message += f"✅ Completed: {order[6]}\n"
        message += "─" * 30 + "\n"
    
    bot.answer_callback_query(call.id, f"Showing {len(all_orders)} orders")
    bot.send_message(call.message.chat.id, message)

@bot.callback_query_handler(func=lambda call: call.data == "admin_complete_order")
def handle_admin_complete_order(call):
    """Ask admin for order ID to complete."""
    bot.answer_callback_query(call.id, "Please send the order ID to complete")
    bot.send_message(call.message.chat.id, "Please send the order ID to complete (e.g., 1, 2, 3):")

@bot.callback_query_handler(func=lambda call: call.data == "admin_allow_orders")
def handle_admin_allow_orders(call):
    """Ask admin for user ID to allow orders."""
    bot.answer_callback_query(call.id, "Please send the user ID to allow orders")
    bot.send_message(call.message.chat.id, "Please send the user ID to allow new orders:")

@bot.callback_query_handler(func=lambda call: call.data == "admin_broadcast")
def handle_admin_broadcast(call):
    """Ask admin for broadcast message."""
    bot.answer_callback_query(call.id, "Please send your broadcast message")
    bot.send_message(call.message.chat.id, "Please send your broadcast message:")

# ================== ADMIN MESSAGE HANDLERS ==================
@bot.message_handler(func=lambda m: m.from_user.id in admin_sessions and m.text.isdigit())
def handle_admin_numeric_input(message):
    """Handle numeric inputs from admin (order ID or user ID)."""
    try:
        number = int(message.text)
        cursor.execute("SELECT id FROM service_orders WHERE id=?", (number,))
        order_exists = cursor.fetchone()
        
        if order_exists:
            success, result = complete_order(number)
            if success:
                bot.send_message(message.chat.id, f"✅ Order #{number} completed successfully!")
            elif result == "already_completed":
                bot.send_message(message.chat.id, f"⚠️ Order #{number} is already completed.")
            else:
                bot.send_message(message.chat.id, f"❌ Order #{number} not found.")
        else:
            cursor.execute("UPDATE user_order_limits SET can_order=1 WHERE user_id=?", (number,))
            conn.commit()
            bot.send_message(message.chat.id, f"✅ User {number} can now place new orders.")
    except ValueError:
        bot.send_message(message.chat.id, "❌ Please enter a valid number.")

@bot.message_handler(func=lambda m: m.from_user.id in admin_sessions and not m.text.startswith('/'))
def handle_admin_broadcast_input(message):
    """Handle broadcast messages from admin."""
    if message.text == ADMIN_PASSWORD or message.text.isdigit():
        return
    
    cursor.execute("SELECT telegram_id FROM users")
    users = cursor.fetchall()
    
    sent_count = 0
    for user in users:
        try:
            bot.send_message(user[0], f"📢 Announcement from Admin:\n\n{message.text}")
            sent_count += 1
        except:
            continue
    
    bot.send_message(message.chat.id, f"✅ Broadcast sent to {sent_count} users.")

# ================== LEGACY HANDLERS ==================
@bot.message_handler(func=lambda m: m.text in ["Communication channels 🌐", "کانال های ارتباطی 🌐"])
def handle_channels(message):
    """Display communication channels."""
    user_id = message.from_user.id
    markup = types.InlineKeyboardMarkup()
    markup.add(
        #Communication channels link
        types.InlineKeyboardButton("Instagram", url=""),
        types.InlineKeyboardButton("x.com", url="")
    )
    markup.add(types.InlineKeyboardButton("Github", url="https://github.com/XenwebDeveloper"))
    bot.send_message(message.chat.id, get_text('channels_title', user_id), reply_markup=markup)

# ================== CONTACT TRACKING ==================
waiting_for_admin_contact = set()

# ================== BOT POLLING ==================
if __name__ == "__main__":
    print("\033[92mThe bot is running. To stop the bot, press Ctrl + C.\033[0m")
    print("\033[93mService Admins Configuration:\033[0m")
    for service, admin_id in SERVICE_ADMINS.items():
        print(f"  {service}: Admin ID = {admin_id}")
    
    try:
        bot.infinity_polling()
    except Exception as e:
        print(f"Error: {e}")
        conn.close()