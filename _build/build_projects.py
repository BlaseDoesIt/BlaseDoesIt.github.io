"""Generates projects/<slug>/index.html for every project below.

Run from the website folder:  python _build/build_projects.py
GitHub Pages ignores folders starting with "_", so this script is not published.
Each text is (english, arabic). Edit here, re-run, commit the generated pages.
"""
import html, json, os

V = "21"  # bump to bust browser caches of style.css / i18n.js

PROJECTS = [
  {
    "slug": "rentory-app",
    "repo": "https://github.com/BlaseDoesIt/rentory-app",
    "wide": True,  # featured card across the top of the home grid
    "gallery": "app",  # desktop shot on top, phone shots below
    "kind": ("Flutter app · phone and desktop", "تطبيق Flutter · الهاتف وسطح المكتب"),
    "title": ("Rentory app", "تطبيق Rentory"),
    "summary": ("A rental management app for phone and desktop. It runs standalone on its own backend, or connects to Odoo 19 when a company already uses it.",
                "تطبيق لإدارة التأجير على الهاتف وسطح المكتب. يعمل مستقلاً على خادمه الخاص، أو يتصل بـ Odoo 19 إن كانت الشركة تستخدمه."),
    "card": ("Orders, pickups, returns and late fees on any phone or computer. Works with or without Odoo.",
             "الطلبات والتسليم والإرجاع وغرامات التأخير على أي هاتف أو كمبيوتر. يعمل مع Odoo أو بدونه."),
    "card_result": ("Android, iPhone, Windows and Mac from one codebase", "Android وiPhone وWindows وMac من كود واحد"),
    "thumb": "rentory-app-desktop.webp",
    "stats": [(("Android", "Android"), ("phones and tablets", "الهواتف والأجهزة اللوحية")),
              (("iPhone", "iPhone"), ("iOS", "iOS")),
              (("Windows", "Windows"), ("desktop", "سطح المكتب")),
              (("Mac", "Mac"), ("desktop", "سطح المكتب"))],
    "before": [("Orders kept in a spreadsheet or a notebook", "الطلبات في جدول بيانات أو دفتر"),
               ("Availability checked by asking around", "التوفر يُعرف بالسؤال"),
               ("Pickup checklist on paper at the warehouse", "قائمة التسليم على الورق في المستودع"),
               ("Late days counted by hand", "أيام التأخير تُحسب يدوياً")],
    "pain": ("Small rental shops can't justify a full ERP, and Odoo screens aren't made for the warehouse floor.",
             "محلات التأجير الصغيرة لا تحتاج نظام ERP كاملاً، وشاشات Odoo لم تُصمَّم لأرض المستودع."),
    "after": [("Order created on a phone or a desktop", "الطلب يُنشأ على الهاتف أو سطح المكتب"),
              ("Units offered only when they're free", "القطع تُعرض فقط عندما تكون متاحة"),
              ("Barcode scan, checklist and signature at pickup", "مسح الباركود وقائمة التحقق والتوقيع عند التسليم"),
              ("Return checked unit by unit, late fee calculated", "الإرجاع يُفحص قطعة بقطعة، وغرامة التأخير تُحسب"),
              ("Saved to its own server, or straight into Odoo", "يُحفظ على خادمه الخاص أو مباشرة في Odoo")],
    "result": ("The same rental workflow runs on any device, with or without Odoo.", "نفس سير عمل التأجير يعمل على أي جهاز، مع Odoo أو بدونه."),
    "features": [("Orders with sections, drag to reorder, and lines booked, picked up or returned one by one", "طلبات بأقسام وترتيب بالسحب، وكل بند يُحجز ويُسلَّم ويُرجع على حدة"),
                 ("Availability per serial, confirmed by the server so no camera is booked twice", "التوفر لكل رقم تسلسلي، يؤكده الخادم فلا تُحجز كاميرا مرتين"),
                 ("Pickup checklist, documents held and customer signature", "قائمة تحقق عند التسليم، الوثائق المحتجزة وتوقيع العميل"),
                 ("Return condition, notes and photos for each unit", "حالة الإرجاع والملاحظات والصور لكل قطعة"),
                 ("Late fees counted automatically, adjustable or waived", "غرامات التأخير تُحسب تلقائياً، ويمكن تعديلها أو إلغاؤها"),
                 ("Camera scanning on phones, USB scanner on desktop", "المسح بالكاميرا على الهاتف، وبقارئ USB على سطح المكتب"),
                 ("In Odoo mode: invoices, payments and printed documents", "في وضع Odoo: الفواتير والدفعات والمستندات المطبوعة"),
                 ("English and Arabic, light and dark", "العربية والإنجليزية، فاتح وداكن")],
    "tech": ["Flutter", "Dart", "Supabase", "SQLite (drift)", "Odoo JSON-2 API"],
    "shots": [("rentory-app-desktop.webp", 1400, 880, ("Orders on desktop", "الطلبات على سطح المكتب")),
              ("rentory-app-phone-orders.webp", 780, 1688, ("Orders on a phone", "الطلبات على الهاتف")),
              ("rentory-app-phone-order.webp", 780, 1688, ("An order with sections", "طلب مقسّم إلى أقسام")),
              ("rentory-app-phone-pickup.webp", 780, 1688, ("Pickup checklist", "قائمة التحقق عند التسليم"))],
  },
  {
    "slug": "rentory",
    "closed": True,  # code stays private; tagged closed-source, no repo link
    "kind": ("Custom Odoo app · rental and assets", "تطبيق Odoo مخصص · التأجير والأصول"),
    "title": ("Odoo Rentory", "Odoo Rentory"),
    "summary": ("A rental and asset management app built inside Odoo 19 for a camera and media equipment rental house.",
                "تطبيق لإدارة التأجير والأصول مبني داخل Odoo 19 لشركة تأجير كاميرات ومعدات إعلامية."),
    "card": ("Orders, equipment, contracts, deposits and late fees in one app.",
             "الطلبات والمعدات والعقود والتأمينات وغرامات التأخير في تطبيق واحد."),
    "card_result": ("No customer request lost since launch", "لم يضع أي طلب عميل منذ الإطلاق"),
    "thumb": "rentory-order.webp",
    "launched": ("Launched on 1 August 2026", "أُطلق في 1 أغسطس 2026"),
    "stats": [(("None", "ولا طلب"), ("customer requests lost since launch", "ضاع من طلبات العملاء منذ الإطلاق")),
              (("Rare", "نادرة"), ("order mistakes, down from several a week", "أخطاء الطلبات، بعد أن كانت متكررة أسبوعياً")),
              (("Almost none", "شبه معدومة"), ("critical incidents in a typical week", "الحوادث الحرجة في الأسبوع المعتاد")),
              ("800+", ("units tracked by serial", "قطعة مُتتبَّعة بالرقم التسلسلي"))],
    "before": [("Customer asks on WhatsApp or by phone", "العميل يسأل عبر واتساب أو الهاتف"),
               ("Order noted on paper or in a chat", "الطلب يُدوَّن على ورقة أو في محادثة"),
               ("Availability checked on the shelf", "التوفر يُفحص على الرف"),
               ("Contracts and IDs checked on paper", "العقود والهويات تُراجع على الورق"),
               ("Late days counted by hand", "أيام التأخير تُحسب يدوياً")],
    "pain": ("Orders and questions got forgotten, and gear rented in from partners wasn't tracked at all.",
             "طلبات وأسئلة كانت تُنسى، والمعدات المستأجرة من الشركاء لم تكن تُتتبع إطلاقاً."),
    "after": [("Order created in Rentory", "الطلب يُنشأ في Rentory"),
              ("Availability checked per serial", "التوفر يُفحص لكل رقم تسلسلي"),
              ("Barcode scanned at pickup", "مسح الباركود عند التسليم"),
              ("Checklist: contract, receipt, ID held", "قائمة تحقق: العقد والإيصال والهوية المحتجزة"),
              ("Return check and late fee calculated", "فحص الإرجاع وحساب غرامة التأخير"),
              ("Invoice created in Odoo", "الفاتورة تُنشأ في Odoo")],
    "result": ("Mistakes went from around 10 to 1 or 2, and no customer request has been lost since launch.",
               "انخفضت الأخطاء من نحو 10 إلى 1 أو 2، ولم يضع أي طلب لعميل منذ الإطلاق."),
    "features": [("Two views in one app: Rental for orders, Assetory for equipment", "واجهتان في تطبيق واحد: Rental للطلبات وAssetory للمعدات"),
                 ("Status, location, rental history and revenue for every serial", "الحالة والموقع وسجل التأجير والإيراد لكل رقم تسلسلي"),
                 ("Equipment rented in from partners, tracked with its supplier", "المعدات المستأجرة من الشركاء تُتتبع مع مورّدها"),
                 ("Deposits held apart from revenue, late fees calculated automatically", "التأمينات منفصلة عن الإيراد، وغرامات التأخير تُحسب تلقائياً"),
                 ("Booking planning on a timeline", "تخطيط الحجوزات على خط زمني"),
                 ("Each unit linked to its fixed asset record in Odoo", "كل قطعة مرتبطة بسجل أصلها الثابت في Odoo"),
                 ("Photos and files at pickup and return", "صور وملفات عند التسليم والإرجاع"),
                 ("Parts, maintenance and retirement of units", "القطع والصيانة وإخراج القطع من الخدمة")],
    "tech": ["Odoo 19 Enterprise", "Python", "OWL / JavaScript", "QWeb", "PostgreSQL"],
    "shots": [("rentory-order.webp", 1224, 924, ("Rental order", "طلب تأجير")),
              ("rentory-lines.webp", 1223, 534, ("Order lines with live availability", "بنود الطلب مع التوفر المباشر")),
              ("rentory-serials.webp", 1255, 817, ("Serials with cost and revenue", "الأرقام التسلسلية مع التكلفة والإيراد")),
              ("rentory-assets.webp", 1400, 787, ("Equipment catalog", "كتالوج المعدات"))],
  },
  {
    "slug": "invoices",
    "repo": "https://github.com/BlaseDoesIt/odoo-arabic-invoices-vouchers",
    "kind": ("Business documents · Arabic", "مستندات أعمال · بالعربية"),
    "title": ("Invoices and vouchers", "الفواتير والسندات"),
    "summary": ("Arabic invoices and receipt or payment vouchers that print straight from Odoo, in the company's own design.",
                "فواتير عربية وسندات قبض ودفع تُطبع مباشرة من Odoo بتصميم الشركة."),
    "card": ("Generated from the order with the amount in Arabic words. No formatting or retyping by hand.", "تُنشأ من الطلب مع المبلغ بالحروف العربية، دون تنسيق أو إعادة كتابة يدوية."),
    "card_result": ("Minutes instead of an hour per document", "دقائق بدل ساعة لكل مستند"),
    "thumb": "voucher.webp",
    "stats": [(("Minutes, not hours", "دقائق لا ساعات"), ("per invoice or voucher, generated from the order instead of formatted and retyped by hand", "لكل فاتورة أو سند، تُنشأ من الطلب بدلاً من تنسيقها وإعادة كتابتها يدوياً")),
              ("120+", ("invoices a month", "فاتورة شهرياً")),
              (("Print-ready", "جاهزة للطباعة"), ("on the A5 stationery already in use", "على قرطاسية A5 المستخدمة حالياً"))],
    "before": [("Open a Word or Excel template", "فتح قالب Word أو Excel"),
               ("Copy items and prices from the order", "نسخ البنود والأسعار من الطلب"),
               ("Write the amount in Arabic words by hand", "كتابة المبلغ بالحروف يدوياً"),
               ("Print, then type it into the system", "الطباعة، ثم إدخاله في النظام")],
    "pain": ("About an hour per document, and the paper didn't always match what was in the system.",
             "نحو ساعة لكل مستند، والورق لم يكن يطابق ما في النظام دائماً."),
    "after": [("Click Print on the order or journal entry", "الضغط على طباعة من الطلب أو قيد اليومية"),
              ("Document generated in the company design", "المستند يُنشأ بتصميم الشركة"),
              ("Amount spelled out in Arabic automatically", "المبلغ يُكتب بالحروف تلقائياً"),
              ("Already recorded in Odoo", "مسجّل في Odoo مسبقاً")],
    "result": ("Each invoice or voucher now takes 2 minutes instead of an hour.", "كل فاتورة أو سند يأخذ الآن دقيقتين بدلاً من ساعة."),
    "features": [("Invoices print from the rental order in the company's design", "الفواتير تُطبع من طلب التأجير بتصميم الشركة"),
                 ("Receipt (سند قبض) and payment (سند دفع) vouchers from any journal entry", "سندات القبض والدفع من أي قيد يومية"),
                 ("Amounts in words with correct Arabic grammar for each currency", "المبالغ بالحروف بقواعد عربية صحيحة لكل عملة"),
                 ("A5 landscape to match the printed stationery", "ورق A5 أفقي ليطابق القرطاسية المطبوعة"),
                 ("Fixed a broken customer label that standard Odoo printed", "إصلاح خلل في اسم العميل كان يظهر في طباعة Odoo الافتراضية")],
    "tech": ["QWeb reports", "Python", "Odoo Invoicing"],
    "shots": [("voucher.webp", 1342, 690, ("Receipt voucher with the amount in Arabic words", "سند قبض مع المبلغ بالحروف")),
              ("invoice.webp", 730, 1015, ("Arabic rental invoice. Customer name hidden.", "فاتورة تأجير عربية. اسم العميل مخفي."))],
  },
  {
    "slug": "shift-guard",
    "repo": "https://github.com/BlaseDoesIt/odoo-attendance-shift-guard",
    "kind": ("Odoo Attendances add-on · HR", "إضافة لتطبيق الحضور في Odoo · موارد بشرية"),
    "title": ("Attendance Shift Guard", "حارس الدوام"),
    "summary": ("GPS-verified attendance with personal shifts, reminders and overtime approval, built on top of Odoo Attendances.",
                "حضور موثّق بـ GPS مع دوامات شخصية وتذكيرات وموافقة على العمل الإضافي، مبني فوق تطبيق الحضور في Odoo."),
    "card": ("GPS check-in, personal shifts, reminders and overtime approval.", "تسجيل حضور بـ GPS، دوامات شخصية، تذكيرات وموافقة على الإضافي."),
    "card_result": ("Replaced a WhatsApp attendance group", "حلّ محل مجموعة واتساب للدوام"),
    "thumb": "attendance.webp",
    "stats": [("50", ("employees covered", "موظفاً مشمولاً")),
              (("Every half hour", "كل نصف ساعة"), ("a reminder until they check in or out", "تذكير حتى يسجّل الدخول أو الخروج")),
              (("No more", "انتهى"), ("hours copied out of a chat", "نسخ الساعات من المحادثات"))],
    "before": [("Employee posts the time in a WhatsApp group", "الموظف يكتب الوقت في مجموعة واتساب"),
               ("Someone reads through the chat", "أحدهم يقرأ المحادثة"),
               ("Hours typed up by hand", "الساعات تُفرَّغ يدوياً"),
               ("Overtime agreed verbally", "العمل الإضافي يُتفق عليه شفهياً")],
    "pain": ("Missing or wrong times, and no proof anyone was actually on site.", "أوقات ناقصة أو خاطئة، ولا دليل على وجود أحد في الموقع فعلاً."),
    "after": [("Employee checks in on Odoo", "الموظف يسجّل حضوره في Odoo"),
              ("GPS geofence confirms they're on site", "السياج الجغرافي يؤكد وجوده في الموقع"),
              ("Reminder if they forget to check in or out", "تذكير إن نسي تسجيل الدخول أو الخروج"),
              ("Overtime requested, manager approves", "طلب عمل إضافي، والمدير يوافق"),
              ("Hours written into attendance", "الساعات تُكتب في سجل الحضور")],
    "result": ("Working hours now come from verified records, not chat messages.", "ساعات العمل تأتي الآن من سجلات موثّقة، لا من رسائل المحادثة."),
    "features": [("Personal shifts: weekday lines, tolerance windows, breaks, overnight and flexible hours", "دوامات شخصية: أيام الأسبوع، هامش السماح، الاستراحات، الدوام الليلي والمرن"),
                 ("GPS geofence around each work location, with trusted network as a fallback", "سياج جغرافي حول كل موقع عمل، مع شبكة موثوقة كبديل"),
                 ("Reminders every 30 minutes, configurable", "تذكيرات كل 30 دقيقة، قابلة للتعديل"),
                 ("Overtime requests with a reason and manager approval", "طلبات عمل إضافي مع السبب وموافقة المدير"),
                 ("Presence log for every check", "سجل حضور لكل عملية تحقق")],
    "tech": ["Python", "OWL / JavaScript", "Geolocation", "Scheduled actions", "Odoo Attendances"],
    "shots": [("attendance.webp", 1400, 514, ("Presence log with GPS distance. Names hidden.", "سجل الحضور مع المسافة عبر GPS. الأسماء مخفية."))],
  },
  {
    "slug": "discounts",
    "repo": "https://github.com/BlaseDoesIt/odoo-rental-customer-discount",
    "small": True,  # shown in "Smaller work" on the home page, no own page
    "kind": ("Odoo Rental add-on · sales", "إضافة لتطبيق التأجير في Odoo · مبيعات"),
    "title": ("Customer discounts", "خصومات العملاء"),
    "summary": ("Fixed discounts per customer, applied automatically to every line of every rental order.",
                "خصومات ثابتة لكل عميل، تُطبَّق تلقائياً على كل بند في كل طلب تأجير."),
    "card": ("Set a customer's discount once, applied to every order.", "اضبط خصم العميل مرة واحدة، فيُطبَّق على كل طلب."),
    "card_result": ("No more forgotten or wrong discounts", "لا خصومات منسية أو خاطئة بعد اليوم"),
    "thumb": "discount.webp",
    "stats": [("1", ("place to set each discount", "مكان واحد لضبط كل خصم")),
              ("100%", ("of order lines covered", "من بنود الطلب مشمولة"))],
    "before": [("Staff remember who gets a discount", "الموظفون يتذكرون من له خصم"),
               ("Discount typed on each order line", "الخصم يُكتب على كل بند"),
               ("Checked again at invoicing", "يُراجع مجدداً عند الفوترة")],
    "pain": ("Discounts were forgotten or entered wrong, and regular customers noticed.", "خصومات تُنسى أو تُدخل خطأً، والعملاء الدائمون يلاحظون."),
    "after": [("Discount set once per customer", "الخصم يُضبط مرة لكل عميل"),
              ("Customer picked on the order", "اختيار العميل في الطلب"),
              ("Applied to every line automatically", "يُطبَّق على كل بند تلقائياً")],
    "result": ("Every regular customer gets the right discount, every time.", "كل عميل دائم يحصل على خصمه الصحيح، في كل مرة."),
    "features": [("Customer Discounts page under Rental configuration", "صفحة خصومات العملاء ضمن إعدادات التأجير"),
                 ("Applied only to rental orders, sales orders untouched", "تُطبَّق على طلبات التأجير فقط دون المساس بطلبات البيع"),
                 ("New lines added later get the discount too", "البنود المضافة لاحقاً تأخذ الخصم أيضاً")],
    "tech": ["Python", "Odoo Rental"],
    "shots": [("discount.webp", 382, 503, ("15% customer discount applied on an order", "خصم عميل 15% مطبّق على طلب"))],
  },
  {
    "slug": "analytics",
    "repo": "https://github.com/BlaseDoesIt/odoo-rental-revenue-analytics",
    "kind": ("Odoo reporting · rental data", "تقارير Odoo · بيانات التأجير"),
    "title": ("Revenue analytics", "تحليلات الإيرادات"),
    "summary": ("Revenue and most-rented reports by month, year, category, customer and serial, inside Odoo.",
                "تقارير الإيرادات والأكثر تأجيراً حسب الشهر والسنة والفئة والعميل والرقم التسلسلي، داخل Odoo."),
    "card": ("Revenue and most-rented reports, one click away.", "تقارير الإيرادات والأكثر تأجيراً بنقرة واحدة."),
    "card_result": ("Investor reports without spreadsheets", "تقارير المستثمرين دون جداول Excel"),
    "thumb": "revenue.webp",
    "stats": [(("Chart · Pivot · List", "رسم · محوري · قائمة"), ("switch views in one click", "التبديل بين العروض بنقرة")),
              (("Any angle", "من كل زاوية"), ("group by product, category, customer, month or year", "التجميع حسب المنتج أو الفئة أو العميل أو الشهر أو السنة"))],
    "before": [("Export orders to Excel", "تصدير الطلبات إلى Excel"),
               ("Add up revenue per item by hand", "جمع إيراد كل قطعة يدوياً"),
               ("Build charts for the investor report", "إعداد رسوم بيانية لتقرير المستثمرين")],
    "pain": ("Days of work, and the numbers were already out of date when the report was done.", "أيام من العمل، والأرقام قديمة عند انتهاء التقرير."),
    "after": [("Open the report in Odoo", "فتح التقرير في Odoo"),
              ("Filter by month, year or all time", "التصفية حسب الشهر أو السنة أو كل الفترات"),
              ("Switch between chart, pivot and list", "التبديل بين الرسم والجدول المحوري والقائمة"),
              ("Insert straight into a spreadsheet", "الإدراج مباشرة في جدول بيانات")],
    "result": ("Live numbers for management and investors, without rebuilding a spreadsheet every month.", "أرقام حيّة للإدارة والمستثمرين، دون إعادة بناء جدول كل شهر."),
    "features": [("Most rented products this month, this year or all time", "المنتجات الأكثر تأجيراً هذا الشهر أو هذه السنة أو كل الفترات"),
                 ("Paid revenue by category, customer and serial", "الإيرادات المدفوعة حسب الفئة والعميل والرقم التسلسلي"),
                 ("Built as a read-only SQL report, so it's fast", "مبني كتقرير SQL للقراءة فقط، لذلك هو سريع")],
    "tech": ["SQL views", "Python", "Odoo reporting"],
    "shots": [("revenue.webp", 1400, 662, ("Paid revenue by equipment category", "الإيرادات المدفوعة حسب فئة المعدات"))],
  },
  {
    "slug": "upgrade",
    "small": True,
    "kind": ("Migration · Odoo.sh", "ترحيل · Odoo.sh"),
    "title": ("Odoo 17 → 19 upgrade", "الترقية من Odoo 17 إلى 19"),
    "summary": ("Moved the company's live database and custom modules from Odoo 17 to Odoo 19 Enterprise on Odoo.sh.",
                "نقل قاعدة بيانات الشركة الحية ووحداتها المخصصة من Odoo 17 إلى Odoo 19 Enterprise على Odoo.sh."),
    "card": ("A live company database moved two versions forward.", "قاعدة بيانات شركة حية نُقلت إصدارين للأمام."),
    "thumb": None,
    "stats": [("17 → 19", ("Odoo versions", "إصدارات Odoo")),
              ("6", ("custom modules running on 19", "وحدات مخصصة تعمل على 19"))],
    "before": [("Company running on Odoo 17", "الشركة تعمل على Odoo 17"),
               ("Custom modules written for 17", "وحدات مخصصة مكتوبة للإصدار 17")],
    "pain": ("Staying on an old version means missing features and a harder upgrade later.", "البقاء على إصدار قديم يعني ميزات مفقودة وترقية أصعب لاحقاً."),
    "after": [("Modules ported and tested", "نقل الوحدات واختبارها"),
              ("Data checked against the old system", "مطابقة البيانات مع النظام القديم"),
              ("Production switched to 19", "تحويل الإنتاج إلى 19")],
    "result": ("The company runs on Odoo 19 Enterprise with all its custom modules.", "الشركة تعمل على Odoo 19 Enterprise مع كل وحداتها المخصصة."),
    "features": [("Custom modules updated to the new version", "تحديث الوحدات المخصصة للإصدار الجديد"),
                 ("Invoice and rental data checked after the move", "مطابقة بيانات الفواتير والتأجير بعد النقل")],
    "tech": ["Odoo.sh", "Odoo 19 Enterprise", "Python", "PostgreSQL"],
    "shots": [],
  },
]

UI = {
  "brand": ("Kosai Alhafez", "قصي الحافظ"),
  "cta": ("Book a call", "احجز مكالمة"),
  "back": ("← All projects", "→ كل المشاريع"),
  "flow_h": ("Before and after", "قبل وبعد"),
  "before": ("Before", "قبل"),
  "after": ("After", "بعد"),
  "problem": ("Problem", "المشكلة"),
  "result": ("Result", "النتيجة"),
  "feat_h": ("What it does", "ما الذي يفعله"),
  "tech_h": ("Built with", "بُني باستخدام"),
  "shots_h": ("Screenshots", "لقطات الشاشة"),
  "src_btn": ("View the source code ↗", "عرض الكود المصدري ↗"),
  "src_link": ("Source code ↗", "الكود المصدري ↗"),
  "open_src": ("OPEN-SOURCE", "مفتوح المصدر"),
  "closed_src": ("CLOSED-SOURCE", "مغلق المصدر"),
  "next": ("Next project", "المشروع التالي"),
  "need_h": ("Need something like this?", "تحتاج شيئاً مشابهاً؟"),
  "need_p": ("Tell me what your team does by hand today. A 15 minute call is enough to see if I can automate it.",
             "أخبرني ما الذي يفعله فريقك يدوياً اليوم. مكالمة 15 دقيقة كافية لنعرف إن كان بإمكاني أتمتته."),
  "need_btn": ("Book a free 15 min call", "احجز مكالمة مجانية 15 دقيقة"),
  "foot": ("© 2026 MHD Kosai Alhafez", "© 2026 محمد قصي الحافظ"),
}

e = html.escape

class Page:
    def __init__(self): self.ar = {}; self.n = 0
    def t(self, pair, tag="span", cls="", key=None):
        en, ar = pair
        if key is None: self.n += 1; key = f"k{self.n}"
        self.ar[key] = e(ar)
        c = f' class="{cls}"' if cls else ""
        return f'<{tag}{c} data-i18n="{key}">{e(en)}</{tag}>'

def lane(p, steps, kind, end_pair, end_kind, start=0):
    # --i staggers the entrance animation across both lanes; .sheen is the hover shine layer
    nodes = "".join(
        f'<li class="node {kind}" style="--i:{start+i}"><i class="sheen"></i><span class="num">{i+1:02d}</span>{p.t(s)}</li>' for i, s in enumerate(steps))
    end = f'<li class="node {end_kind}" style="--i:{start+len(steps)}"><i class="sheen"></i><span class="num">{p.t(UI["problem" if end_kind=="pain" else "result"], key="u_"+end_kind)}</span>{p.t(end_pair)}</li>'
    return f'<ol class="lane">{nodes}{end}</ol>'

def build(proj, nxt):
    p = Page()
    for k, v in UI.items(): p.ar["u_" + k] = e(v[1])
    T = lambda k, **kw: p.t(UI[k], key="u_" + k, **kw)
    title_en, title_ar = proj["title"]
    stats = "".join(
        f'<div class="stat">{p.t(v, tag="b", cls="w") if isinstance(v, tuple) else f"<b>{e(v)}</b>"}{p.t(l)}</div>'
        for v, l in proj["stats"])
    feats = "".join(f'<li>{p.t(f)}</li>' for f in proj["features"])
    tech = "".join(f'<span class="chip">{e(x)}</span>' for x in proj["tech"])
    src = f'<a class="btn src" href="{proj["repo"]}" target="_blank" rel="noopener" data-i18n="u_src_btn">{e(UI["src_btn"][0])}</a>' if proj.get("repo") else ""
    lk = lic_key(proj)
    lic = f'<span class="lic" data-i18n="u_{lk}">{e(UI[lk][0])}</span>' if lk else ""
    shots = ""
    if proj["shots"]:
        items = "".join(
            f'<figure class="shot"><a href="../../img/{f}" target="_blank"><img src="../../img/{f}" alt="{e(c[0])}" loading="lazy" width="{w}" height="{h}"></a></figure>'
            for f, w, h, c in proj["shots"])
        shots = f'''
  <section>
    <div class="wrap">
      {T("shots_h", tag="h2")}
      <div class="gallery n{len(proj["shots"])}{" " + proj["gallery"] if proj.get("gallery") else ""}">{items}</div>
    </div>
  </section>'''
    flow = f'''<div class="flow">
        <div class="flow-row">{T("before", cls="lane-label b")}{lane(p, proj["before"], "b", proj["pain"], "pain")}</div>
        <div class="flow-bridge" aria-hidden="true"></div>
        <div class="flow-row">{T("after", cls="lane-label a")}{lane(p, proj["after"], "a", proj["result"], "res", len(proj["before"]) + 2)}</div>
      </div>'''
    return f'''<!DOCTYPE html>
<html lang="en" dir="ltr">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>{e(title_en)} | Kosai Alhafez</title>
<meta name="description" content="{e(proj["summary"][0])}">
<meta property="og:title" content="{e(title_en)} | Kosai Alhafez">
<meta property="og:description" content="{e(proj["summary"][0])}">
<meta property="og:image" content="https://blasedoesit.com/img/og.jpg?v=2">
<link rel="icon" href="../../favicon.svg" type="image/svg+xml">
<link rel="icon" href="../../favicon.png" type="image/png" sizes="64x64">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=IBM+Plex+Sans+Arabic:wght@400;500;600&family=Noto+Kufi+Arabic:wght@600;800&display=swap" rel="stylesheet">
<link rel="stylesheet" href="../../style.css?v={V}">
<script>document.documentElement.classList.add("js")</script>
</head>
<body>

<header class="top">
  <div class="wrap">
    <a class="brand" href="../../" data-i18n="u_brand">Kosai Alhafez</a>
    <button class="lang" id="langBtn" type="button">العربية</button>
    <a class="btn solid" href="https://cal.com/kosai/15min" target="_blank" rel="noopener" data-i18n="u_cta">Book a call</a>
  </div>
</header>

<main>
  <div class="wrap hero proj-hero">
    <a class="crumb" href="../../#work" data-i18n="u_back">← All projects</a>
    {lic}
    {p.t(proj["kind"], tag="p", cls="eyebrow")}
    {p.t(proj["title"], tag="h1", cls="page-h1")}
    {p.t(proj["summary"], tag="p", cls="lead")}
    {p.t(proj["launched"], tag="p", cls="launch") if proj.get("launched") else ""}
    <div class="stats n{len(proj["stats"])}">{stats}</div>
  </div>

  <section>
    <div class="wrap">
      {T("flow_h", tag="h2")}
      {flow}
    </div>
  </section>

  <section>
    <div class="wrap feat-grid">
      <div>
        {T("feat_h", tag="h2")}
        <ul class="ticks">{feats}</ul>
      </div>
      <div>
        {T("tech_h", tag="h3")}
        <div class="chips">{tech}</div>
        {src}
      </div>
    </div>
  </section>
{shots}
  <section>
    <div class="wrap next-grid">
      <a class="next-card" href="../{nxt["slug"]}/">
        {T("next", cls="muted")}
        {p.t(nxt["title"], tag="b")}
      </a>
      <div class="need">
        {T("need_h", tag="h3")}
        {T("need_p", tag="p", cls="muted")}
        <a class="btn solid" href="https://cal.com/kosai/15min" target="_blank" rel="noopener" data-i18n="u_need_btn">Book a free 15 min call</a>
      </div>
    </div>
  </section>
</main>

<footer>
  <div class="wrap"><span data-i18n="u_foot">© 2026 MHD Kosai Alhafez</span><span>Damascus · UTC+3</span></div>
</footer>

<script>
window.TITLES = {json.dumps({"en": title_en + " | Kosai Alhafez", "ar": title_ar + " | قصي الحافظ"}, ensure_ascii=False)};
window.AR = {json.dumps(p.ar, ensure_ascii=False, indent=0)};
</script>
<script src="../../i18n.js?v={V}"></script>
<script src="../../anim.js?v={V}"></script>
</body>
</html>
'''

def lic_key(pr):
    """open_src / closed_src label key, or None when there is no code to speak of."""
    return "closed_src" if pr.get("closed") else "open_src" if pr.get("repo") else None

def lic_tag(pr, ar):
    lk = lic_key(pr)
    if not lk: return ""
    ar["lic_" + lk] = e(UI[lk][1])
    return f'<span class="lic" data-i18n="lic_{lk}">{e(UI[lk][0])}</span>'

def cards():
    """Home page markup: project cards, plus the compact "smaller work" items."""
    out, small, ar = [], [], {"sw_h": "أعمال أصغر"}
    for i, pr in enumerate(PROJECTS):
        if pr.get("small"):
            k = f"sw{i}"
            ar[k+"t"], ar[k+"d"] = e(pr["title"][1]), e(pr["card"][1])
            res = ""  # the result line is optional for smaller work
            if pr.get("card_result"):
                ar[k+"r"] = e(pr["card_result"][1])
                res = NL + f'            <span class="pres" data-i18n="{k}r">{e(pr["card_result"][0])}</span>'
            src = ""
            if pr.get("repo"):
                ar["sw_src"] = e(UI["src_link"][1])
                src = NL + f'            <a class="src" href="{pr["repo"]}" target="_blank" rel="noopener" data-i18n="sw_src">{e(UI["src_link"][0])}</a>'
            small.append(f'''          <div class="sw">
            {lic_tag(pr, ar)}<h4 data-i18n="{k}t">{e(pr["title"][0])}</h4>
            <p data-i18n="{k}d">{e(pr["card"][0])}</p>{res}{src}
          </div>''')
            continue
        k = f"pc{i}"
        launch = ""
        if pr.get("launched"):
            ar[k+"l"] = e(pr["launched"][1])
            launch = NL + f'            <span class="launch" data-i18n="{k}l">{e(pr["launched"][0])}</span>'
        ar[k+"k"], ar[k+"t"], ar[k+"d"], ar[k+"r"] = (e(pr["kind"][1]), e(pr["title"][1]), e(pr["card"][1]), e(pr["card_result"][1]))
        out.append(f'''        <a class="pcard{' wide' if pr.get('wide') else ''}" href="projects/{pr["slug"]}/">
          {lic_tag(pr, ar)}
          <div class="thumb"><img src="img/{pr["thumb"]}" alt="" loading="lazy"></div>
          <div class="pbody">
            <span class="kind" data-i18n="{k}k">{e(pr["kind"][0])}</span>
            <h3 data-i18n="{k}t">{e(pr["title"][0])}</h3>
            <p data-i18n="{k}d">{e(pr["card"][0])}</p>{launch}
            <span class="pres" data-i18n="{k}r">{e(pr["card_result"][0])}</span>
          </div>
        </a>''')
    return NL.join(out), NL.join(small), ar

NL = "\n"

def splice(s, a, b, inner):
    return s[:s.index(a) + len(a)] + NL + inner + NL + "        " + s[s.index(b):]

if __name__ == "__main__":
    root = os.path.join(os.path.dirname(__file__), "..")
    big = [pr for pr in PROJECTS if not pr.get("small")]
    for i, pr in enumerate(big):
        d = os.path.join(root, "projects", pr["slug"]); os.makedirs(d, exist_ok=True)
        with open(os.path.join(d, "index.html"), "w", encoding="utf-8", newline=NL) as f:
            f.write(build(pr, big[(i + 1) % len(big)]))
    grid, small, ar = cards()
    ip = os.path.join(root, "index.html")
    s = open(ip, encoding="utf-8").read()
    s = splice(s, "<!-- projects:start -->", "<!-- projects:end -->", grid)
    s = splice(s, "<!-- small:start -->", "<!-- small:end -->", small)
    a, b = "/* project-cards:start */", "/* project-cards:end */"
    s = s[:s.index(a) + len(a)] + NL + "".join(f'  {k}:{json.dumps(v, ensure_ascii=False)},' + NL for k, v in ar.items()) + "  " + s[s.index(b):]
    open(ip, "w", encoding="utf-8", newline=NL).write(s)
    print("built", len(big), "project pages")
