
# Dorks de Braintree mejorados y optimizados
BRAINTREE_DORKS = [
    # Dorks específicos para elementos JavaScript de Braintree
    'intext:"braintree.client.create" OR intext:"braintree.setup" OR intext:"bt.create" (inurl:/shop OR inurl:/store OR inurl:/checkout OR inurl:/payment) -site:braintreepayments.com -site:github.com -site:stackoverflow.com -inurl:/docs -inurl:/tutorial',

    # Dorks para tokens y configuraciones Braintree
    'intext:"client_token" AND (intext:"braintree" OR intext:"dropin") (inurl:/payment OR inurl:/checkout OR inurl:/cart) -site:braintreepayments.com -site:github.com -site:codepen.io',

    # Dorks para bibliotecas y scripts Braintree
    'inurl:"braintree-web" OR inurl:"braintree.min.js" OR inurl:"braintree.js" (inurl:/shop OR inurl:/store OR inurl:/checkout) -site:braintreepayments.com -site:jsdelivr.net -site:unpkg.com',

    # Dorks para elementos HTML específicos de Braintree
    'intext:"id=\"braintree-dropin\"" OR intext:"class=\"braintree\"" OR intext:"data-braintree" (inurl:/checkout OR inurl:/payment OR inurl:/billing) -site:braintreepayments.com',

    # Dorks para métodos de pago Braintree con PayPal
    'intext:"braintree" AND (intext:"paypal" OR intext:"venmo") AND (inurl:/shop OR inurl:/store OR inurl:/buy) -site:braintreepayments.com -site:paypal.com',

    # Dorks para formularios de pago con Braintree
    'intext:"braintree.dropin" OR intext:"bt.dropin" (intext:"credit card" OR intext:"payment form") -site:braintreepayments.com -site:github.com',

    # Dorks para tiendas de ropa con Braintree
    '(intext:"fashion" OR intext:"clothing" OR intext:"apparel") AND (intext:"braintree" OR intext:"braintreegateway") (inurl:/shop OR inurl:/store) -site:braintreepayments.com',

    # Dorks para tiendas de tecnología con Braintree
    '(intext:"electronics" OR intext:"gadgets" OR intext:"tech") AND intext:"braintree" (inurl:/buy OR inurl:/purchase OR inurl:/order) -site:braintreepayments.com',

    # Dorks para ecommerce con sandbox de Braintree
    'intext:"sandbox" AND intext:"braintree" (inurl:/test OR inurl:/demo OR inurl:/staging) -site:braintreepayments.com',

    # Dorks para sitios con procesamiento de pagos Braintree
    'intext:"payment_method_nonce" AND intext:"braintree" (inurl:/process OR inurl:/submit OR inurl:/complete) -site:braintreepayments.com',

    # Dorks para APIs de Braintree en sitios de comercio
    'intext:"client.request" AND intext:"braintree" (inurl:/api OR inurl:/payment OR inurl:/transaction) -site:braintreepayments.com -site:github.com',

    # Dorks para módulos específicos de Braintree
    'intext:"braintree.threeDSecure" OR intext:"braintree.applePay" OR intext:"braintree.googlePay" -site:braintreepayments.com -site:github.com',

    # Dorks para sitios de suscripción con Braintree
    'intext:"subscription" AND intext:"braintree" (inurl:/subscribe OR inurl:/plan OR inurl:/billing) -site:braintreepayments.com',

    # Dorks para marketplace con Braintree
    'intext:"marketplace" AND intext:"braintree" (inurl:/vendor OR inurl:/seller OR inurl:/merchant) -site:braintreepayments.com',

    # Dorks genéricos mejorados para Braintree
    '(intext:"powered by braintree" OR intext:"secured by braintree") (inurl:/shop OR inurl:/store OR inurl:/checkout) -site:braintreepayments.com',

    # Dorks para errores de Braintree que revelan implementaciones
    'intext:"braintree error" OR intext:"braintree failed" (inurl:/checkout OR inurl:/payment) -site:braintreepayments.com -site:github.com',

    # Dorks para webhooks de Braintree
    'intext:"braintree webhook" OR intext:"webhook_notification" (inurl:/webhook OR inurl:/notify OR inurl:/callback) -site:braintreepayments.com',

    # Dorks para configuraciones específicas de Braintree
    'intext:"environment: \"sandbox\"" OR intext:"environment: \"production\"" AND intext:"braintree" -site:braintreepayments.com -site:github.com',

    # Nuevos dorks específicos por industria
    '(intext:"jewelry" OR intext:"accessories") AND intext:"braintree" (inurl:/shop OR inurl:/store) -site:braintreepayments.com',
    '(intext:"books" OR intext:"publishing") AND intext:"braintree" (inurl:/shop OR inurl:/store) -site:braintreepayments.com',
    '(intext:"fitness" OR intext:"gym" OR intext:"workout") AND intext:"braintree" (inurl:/membership OR inurl:/subscribe) -site:braintreepayments.com',

    # Dorks específicos para sitios .org - Organizaciones y tiendas
    'site:.org (inurl:/shop OR inurl:/store OR inurl:/checkout) (intext:"braintree" OR intext:"braintree.client") (intext:"nonprofit" OR "charity" OR "foundation") -site:braintreepayments.com -site:github.com',
    'site:.org (inurl:/donate OR inurl:/donation OR inurl:/give) (intext:"braintree" OR intext:"braintree.dropin") -site:braintreepayments.com -site:github.com',
    'site:.org (inurl:/merchandise OR inurl:/merch OR inurl:/gift) (intext:"braintree" OR intext:"braintree.client") -site:braintreepayments.com -site:github.com',
    'site:.org (intext:"museum store" OR "museum shop") (intext:"braintree" OR intext:"braintree.dropin") -site:braintreepayments.com -site:github.com',
    'site:.org (intext:"university store" OR "college store") (intext:"braintree" OR intext:"braintree.client") -site:braintreepayments.com -site:github.com',
    'site:.org (intext:"church store" OR "religious store") (intext:"braintree" OR intext:"braintree.dropin") -site:braintreepayments.com -site:github.com',
    'site:.org (intext:"wildlife" OR "conservation" OR "environment") (inurl:/shop OR inurl:/store) (intext:"braintree" OR intext:"braintree.client") -site:braintreepayments.com',
    'site:.org (intext:"art gallery" OR "artist" OR "craft") (inurl:/shop OR inurl:/store) (intext:"braintree" OR intext:"braintree.dropin") -site:braintreepayments.com',
    'site:.org (intext:"community" OR "local" OR "neighborhood") (inurl:/shop OR inurl:/store) (intext:"braintree" OR intext:"braintree.client") -site:braintreepayments.com',
    'site:.org (intext:"health" OR "medical" OR "wellness") (inurl:/shop OR inurl:/store) (intext:"braintree" OR intext:"braintree.dropin") -site:braintreepayments.com',
    'site:.org (intext:"education" OR "school" OR "learning") (inurl:/shop OR inurl:/store) (intext:"braintree" OR intext:"braintree.client") -site:braintreepayments.com',
    'site:.org (intext:"sports club" OR "athletic" OR "team") (inurl:/shop OR inurl:/store) (intext:"braintree" OR intext:"braintree.dropin") -site:braintreepayments.com',
    'site:.org (intext:"library" OR "book" OR "reading") (inurl:/shop OR inurl:/store) (intext:"braintree" OR intext:"braintree.client") -site:braintreepayments.com',
    'site:.org (intext:"festival" OR "event" OR "conference") (inurl:/shop OR inurl:/store OR inurl:/ticket) (intext:"braintree" OR intext:"braintree.dropin") -site:braintreepayments.com',
    'site:.org (intext:"volunteer" OR "service" OR "humanitarian") (inurl:/shop OR inurl:/store) (intext:"braintree" OR intext:"braintree.client") -site:braintreepayments.com'
]

# Dorks de Authorize.Net organizados por categorías
AUTH_NET_DORKS = [
    # Plantas y jardinería
    '(inurl:/shop OR inurl:/store OR inurl:/product OR inurl:/checkout OR inurl:/cart) (intext:"authorize.net" OR intext:"authorizenet" OR intext:"acceptjs" OR intext:"accept.js") (intext:"plant" OR "succulent" OR "cactus" OR "bonsai" OR "garden" OR "gardening" OR "nursery" OR "flower" OR "botanical" OR "houseplant" OR "terrarium" OR "fertilizer" OR "soil" OR "seeds") -site:authorize.net -site:github.com -site:reddit.com -site:facebook.com -site:twitter.com -site:linkedin.com -site:instagram.com -inurl:/docs -inurl:/developer -inurl:/partners -inurl:/plugins -inurl:/integration -intext:"payment gateway" -intext:"reseller" -intext:"accept payments for clients" -intitle:"API" -intitle:"Documentation" (site:.com OR site:.org) after:2023',

    # Ropa y moda
    '(inurl:/shop OR inurl:/store OR inurl:/product OR inurl:/checkout OR inurl:/cart) (intext:"authorize.net" OR intext:"authorizenet" OR intext:"acceptjs" OR intext:"accept.js") (intext:"clothing" OR "fashion" OR "apparel" OR "t-shirt" OR "shoes" OR "sneakers" OR "streetwear") -site:authorize.net -site:github.com -site:reddit.com -site:facebook.com -site:twitter.com -site:linkedin.com -site:instagram.com -inurl:/docs -inurl:/developer -inurl:/partners -inurl:/plugins -inurl:/integration -intext:"payment gateway" -intext:"reseller" -intext:"accept payments for clients" -intitle:"API" -intitle:"Documentation" (site:.com OR site:.org) after:2023',

    # Tecnología y gadgets
    '(inurl:/shop OR inurl:/store OR inurl:/product OR inurl:/checkout OR inurl:/cart) (intext:"authorize.net" OR intext:"authorizenet" OR intext:"acceptjs" OR intext:"accept.js") (intext:"electronics" OR "gadgets" OR "tech" OR "laptop" OR "phone" OR "charger" OR "smartwatch" OR "tablet" OR "device") -site:authorize.net -site:github.com -site:reddit.com -site:facebook.com -site:twitter.com -site:linkedin.com -site:instagram.com -inurl:/docs -inurl:/developer -inurl:/partners -inurl:/plugins -inurl:/integration -intext:"payment gateway" -intext:"reseller" -intext:"accept payments for clients" -intitle:"API" -intitle:"Documentation" (site:.com OR site:.org) after:2023',

    # Herramientas y construcción
    '(inurl:/shop OR inurl:/store OR inurl:/product OR inurl:/checkout OR inurl:/cart) (intext:"authorize.net" OR intext:"authorizenet" OR intext:"acceptjs" OR intext:"accept.js") (intext:"tools" OR "tool" OR "drill" OR "saw" OR "hammer" OR "construction" OR "hardware" OR "power tools" OR "screwdriver" OR "wrench") -site:authorize.net -site:github.com -site:reddit.com -site:facebook.com -site:twitter.com -site:linkedin.com -site:instagram.com -inurl:/docs -inurl:/developer -inurl:/partners -inurl:/plugins -inurl:/integration -intext:"payment gateway" -intext:"reseller" -intext:"accept payments for clients" -intitle:"API" -intitle:"Documentation" (site:.com OR site:.org) after:2023',

    # Libros y educación
    '(inurl:/shop OR inurl:/store OR inurl:/product OR inurl:/checkout OR inurl:/cart) (intext:"authorize.net" OR intext:"authorizenet" OR intext:"acceptjs" OR intext:"accept.js") (intext:"book" OR "books" OR "novel" OR "literature" OR "reading" OR "study" OR "learning" OR "course" OR "ebook") -site:authorize.net -site:github.com -site:reddit.com -site:facebook.com -site:twitter.com -site:linkedin.com -site:instagram.com -inurl:/docs -inurl:/developer -inurl:/partners -inurl:/plugins -inurl:/integration -intext:"payment gateway" -intext:"reseller" -intext:"accept payments for clients" -intitle:"API" -intitle:"Documentation" (site:.com OR site:.org) after:2023',

    # Mascotas
    '(inurl:/shop OR inurl:/store OR inurl:/product OR inurl:/checkout OR inurl:/cart) (intext:"authorize.net" OR intext:"authorizenet" OR intext:"acceptjs" OR intext:"accept.js") (intext:"pet" OR "pets" OR "dog" OR "cat" OR "leash" OR "pet toy" OR "collar" OR "treats" OR "pet food") -site:authorize.net -site:github.com -site:reddit.com -site:facebook.com -site:twitter.com -site:linkedin.com -site:instagram.com -inurl:/docs -inurl:/developer -inurl:/partners -inurl:/plugins -inurl:/integration -intext:"payment gateway" -intext:"reseller" -intext:"accept payments for clients" -intitle:"API" -intitle:"Documentation" (site:.com OR site:.org) after:2023',

    # Comida y bebida
    '(inurl:/shop OR inurl:/store OR inurl:/product OR inurl:/checkout OR inurl:/cart) (intext:"authorize.net" OR intext:"authorizenet" OR intext:"acceptjs" OR intext:"accept.js") (intext:"chocolate" OR "snack" OR "coffee" OR "tea" OR "organic" OR "vegan" OR "honey" OR "spice" OR "gourmet" OR "wine") -site:authorize.net -site:github.com -site:reddit.com -site:facebook.com -site:twitter.com -site:linkedin.com -site:instagram.com -inurl:/docs -inurl:/developer -inurl:/partners -inurl:/plugins -inurl:/integration -intext:"payment gateway" -intext:"reseller" -intext:"accept payments for clients" -intitle:"API" -intitle:"Documentation" (site:.com OR site:.org) after:2023',

    # Videojuegos y entretenimiento
    '(inurl:/shop OR inurl:/store OR inurl:/product OR inurl:/checkout OR inurl:/cart) (intext:"authorize.net" OR intext:"authorizenet" OR intext:"acceptjs" OR intext:"accept.js") (intext:"gaming" OR "games" OR "gamepad" OR "console" OR "PC game" OR "video game" OR "playstation" OR "xbox") -site:authorize.net -site:github.com -site:reddit.com -site:facebook.com -site:twitter.com -site:linkedin.com -site:instagram.com -inurl:/docs -inurl:/developer -inurl:/partners -inurl:/plugins -inurl:/integration -intext:"payment gateway" -intext:"reseller" -intext:"accept payments for clients" -intitle:"API" -intitle:"Documentation" (site:.com OR site:.org) after:2023',

    # Arte, diseño y decoración
    '(inurl:/shop OR inurl:/store OR inurl:/product OR inurl:/checkout OR inurl:/cart) (intext:"authorize.net" OR intext:"authorizenet" OR intext:"acceptjs" OR intext:"accept.js") (intext:"art" OR "prints" OR "canvas" OR "poster" OR "illustration" OR "decor" OR "home design" OR "interior") -site:authorize.net -site:github.com -site:reddit.com -site:facebook.com -site:twitter.com -site:linkedin.com -site:instagram.com -inurl:/docs -inurl:/developer -inurl:/partners -inurl:/plugins -inurl:/integration -intext:"payment gateway" -intext:"reseller" -intext:"accept payments for clients" -intitle:"API" -intitle:"Documentation" (site:.com OR site:.org) after:2023',

    # Joyas y accesorios
    '(inurl:/shop OR inurl:/store OR inurl:/product OR inurl:/checkout OR inurl:/cart) (intext:"authorize.net" OR intext:"authorizenet" OR intext:"acceptjs" OR intext:"accept.js") (intext:"jewelry" OR "jewellery" OR "necklace" OR "ring" OR "bracelet" OR "earrings" OR "watch" OR "accessories") -site:authorize.net -site:github.com -site:reddit.com -site:facebook.com -site:twitter.com -site:linkedin.com -site:instagram.com -inurl:/docs -inurl:/developer -inurl:/partners -inurl:/plugins -inurl:/integration -intext:"payment gateway" -intext:"reseller" -intext:"accept payments for clients" -intitle:"API" -intitle:"Documentation" (site:.com OR site:.org) after:2023',

    # Deportes y fitness
    '(inurl:/shop OR inurl:/store OR inurl:/product OR inurl:/checkout OR inurl:/cart) (intext:"authorize.net" OR intext:"authorizenet" OR intext:"acceptjs" OR intext:"accept.js") (intext:"sports" OR "fitness" OR "gym" OR "workout" OR "athletic" OR "running" OR "yoga" OR "exercise") -site:authorize.net -site:github.com -site:reddit.com -site:facebook.com -site:twitter.com -site:linkedin.com -site:instagram.com -inurl:/docs -inurl:/developer -inurl:/partners -inurl:/plugins -inurl:/integration -intext:"payment gateway" -intext:"reseller" -intext:"accept payments for clients" -intitle:"API" -intitle:"Documentation" (site:.com OR site:.org) after:2023',

    # Salud y belleza
    '(inurl:/shop OR inurl:/store OR inurl:/product OR inurl:/checkout OR inurl:/cart) (intext:"authorize.net" OR intext:"authorizenet" OR intext:"acceptjs" OR intext:"accept.js") (intext:"beauty" OR "cosmetics" OR "skincare" OR "makeup" OR "health" OR "supplements" OR "vitamins") -site:authorize.net -site:github.com -site:reddit.com -site:facebook.com -site:twitter.com -site:linkedin.com -site:instagram.com -inurl:/docs -inurl:/developer -inurl:/partners -inurl:/plugins -inurl:/integration -intext:"payment gateway" -intext:"reseller" -intext:"accept payments for clients" -intitle:"API" -intitle:"Documentation" (site:.com OR site:.org) after:2023',

    # Automotriz
    '(inurl:/shop OR inurl:/store OR inurl:/product OR inurl:/checkout OR inurl:/cart) (intext:"authorize.net" OR intext:"authorizenet" OR intext:"acceptjs" OR intext:"accept.js") (intext:"automotive" OR "car parts" OR "motorcycle" OR "auto accessories" OR "tires" OR "battery") -site:authorize.net -site:github.com -site:reddit.com -site:facebook.com -site:twitter.com -site:linkedin.com -site:instagram.com -inurl:/docs -inurl:/developer -inurl:/partners -inurl:/plugins -inurl:/integration -intext:"payment gateway" -intext:"reseller" -intext:"accept payments for clients" -intitle:"API" -intitle:"Documentation" (site:.com OR site:.org) after:2023',

    # Hogar y muebles
    '(inurl:/shop OR inurl:/store OR inurl:/product OR inurl:/checkout OR inurl:/cart) (intext:"authorize.net" OR intext:"authorizenet" OR intext:"acceptjs" OR intext:"accept.js") (intext:"furniture" OR "home goods" OR "kitchen" OR "appliances" OR "bedding" OR "lighting") -site:authorize.net -site:github.com -site:reddit.com -site:facebook.com -site:twitter.com -site:linkedin.com -site:instagram.com -inurl:/docs -inurl:/developer -inurl:/partners -inurl:/plugins -inurl:/integration -intext:"payment gateway" -intext:"reseller" -intext:"accept payments for clients" -intitle:"API" -intitle:"Documentation" (site:.com OR site:.org) after:2023',

    # Música y instrumentos
    '(inurl:/shop OR inurl:/store OR inurl:/product OR inurl:/checkout OR inurl:/cart) (intext:"authorize.net" OR intext:"authorizenet" OR intext:"acceptjs" OR intext:"accept.js") (intext:"music" OR "instruments" OR "guitar" OR "piano" OR "drums" OR "audio equipment") -site:authorize.net -site:github.com -site:reddit.com -site:facebook.com -site:twitter.com -site:linkedin.com -site:instagram.com -inurl:/docs -inurl:/developer -inurl:/partners -inurl:/plugins -inurl:/integration -intext:"payment gateway" -intext:"reseller" -intext:"accept payments for clients" -intitle:"API" -intitle:"Documentation" (site:.com OR site:.org) after:2023',

    # Bebés y niños
    '(inurl:/shop OR inurl:/store OR inurl:/product OR inurl:/checkout OR inurl:/cart) (intext:"authorize.net" OR intext:"authorizenet" OR intext:"acceptjs" OR intext:"accept.js") (intext:"baby" OR "kids" OR "children" OR "toys" OR "stroller" OR "diapers" OR "nursery") -site:authorize.net -site:github.com -site:reddit.com -site:facebook.com -site:twitter.com -site:linkedin.com -site:instagram.com -inurl:/docs -inurl:/developer -inurl:/partners -inurl:/plugins -inurl:/integration -intext:"payment gateway" -intext:"reseller" -intext:"accept payments for clients" -intitle:"API" -intitle:"Documentation" (site:.com OR site:.org) after:2023',

    # Outdoor y camping
    '(inurl:/shop OR inurl:/store OR inurl:/product OR inurl:/checkout OR inurl:/cart) (intext:"authorize.net" OR intext:"authorizenet" OR intext:"acceptjs" OR intext:"accept.js") (intext:"outdoor" OR "camping" OR "hiking" OR "fishing" OR "hunting" OR "survival gear") -site:authorize.net -site:github.com -site:reddit.com -site:facebook.com -site:twitter.com -site:linkedin.com -site:instagram.com -inurl:/docs -inurl:/developer -inurl:/partners -inurl:/plugins -inurl:/integration -intext:"payment gateway" -intext:"reseller" -intext:"accept payments for clients" -intitle:"API" -intitle:"Documentation" (site:.com OR site:.org) after:2023',

    # Oficina y papelería
    '(inurl:/shop OR inurl:/store OR inurl:/product OR inurl:/checkout OR inurl:/cart) (intext:"authorize.net" OR intext:"authorizenet" OR intext:"acceptjs" OR intext:"accept.js") (intext:"office supplies" OR "stationery" OR "printer" OR "desk" OR "chair" OR "notebook") -site:authorize.net -site:github.com -site:reddit.com -site:facebook.com -site:twitter.com -site:linkedin.com -site:instagram.com -inurl:/docs -inurl:/developer -inurl:/partners -inurl:/plugins -inurl:/integration -intext:"payment gateway" -intext:"reseller" -intext:"accept payments for clients" -intitle:"API" -intitle:"Documentation" (site:.com OR site:.org) after:2023',

    # Dorks genéricos adicionales
    '(inurl:/shop OR inurl:/store OR inurl:/product OR inurl:/checkout OR inurl:/cart) (intext:"authorize.net" OR intext:"authorizenet" OR intext:"acceptjs" OR intext:"accept.js") -site:authorize.net -site:github.com -site:reddit.com -site:facebook.com -site:twitter.com -site:linkedin.com -site:instagram.com -inurl:/docs -inurl:/developer -inurl:/partners -inurl:/plugins -inurl:/integration -intext:"payment gateway" -intext:"reseller" -intext:"accept payments for clients" -intitle:"API" -intitle:"Documentation" (site:.com OR site:.org) after:2023',

    # Dorks específicos para sitios .org - Organizaciones y tiendas
    'site:.org (inurl:/shop OR inurl:/store OR inurl:/checkout) (intext:"authorize.net" OR intext:"authorizenet") (intext:"nonprofit" OR "charity" OR "foundation" OR "organization") -site:authorize.net -site:github.com',
    'site:.org (inurl:/donate OR inurl:/donation OR inurl:/give) (intext:"authorize.net" OR intext:"authorizenet") -site:authorize.net -site:github.com',
    'site:.org (inurl:/merchandise OR inurl:/merch OR inurl:/gift) (intext:"authorize.net" OR intext:"authorizenet") -site:authorize.net -site:github.com',
    'site:.org (intext:"museum store" OR "museum shop") (intext:"authorize.net" OR intext:"authorizenet") -site:authorize.net -site:github.com',
    'site:.org (intext:"university store" OR "college store") (intext:"authorize.net" OR intext:"authorizenet") -site:authorize.net -site:github.com',
    'site:.org (intext:"church store" OR "religious store") (intext:"authorize.net" OR intext:"authorizenet") -site:authorize.net -site:github.com',
    'site:.org (intext:"wildlife" OR "conservation" OR "environment") (inurl:/shop OR inurl:/store) (intext:"authorize.net" OR intext:"authorizenet") -site:authorize.net',
    'site:.org (intext:"art gallery" OR "artist" OR "craft") (inurl:/shop OR inurl:/store) (intext:"authorize.net" OR intext:"authorizenet") -site:authorize.net',
    'site:.org (intext:"community" OR "local" OR "neighborhood") (inurl:/shop OR inurl:/store) (intext:"authorize.net" OR intext:"authorizenet") -site:authorize.net',
    'site:.org (intext:"health" OR "medical" OR "wellness") (inurl:/shop OR inurl:/store) (intext:"authorize.net" OR intext:"authorizenet") -site:authorize.net',
    'site:.org (intext:"education" OR "school" OR "learning") (inurl:/shop OR inurl:/store) (intext:"authorize.net" OR intext:"authorizenet") -site:authorize.net',
    'site:.org (intext:"sports club" OR "athletic" OR "team") (inurl:/shop OR inurl:/store) (intext:"authorize.net" OR intext:"authorizenet") -site:authorize.net',
    'site:.org (intext:"library" OR "book" OR "reading") (inurl:/shop OR inurl:/store) (intext:"authorize.net" OR intext:"authorizenet") -site:authorize.net',
    'site:.org (intext:"festival" OR "event" OR "conference") (inurl:/shop OR inurl:/store OR inurl:/ticket) (intext:"authorize.net" OR intext:"authorizenet") -site:authorize.net',
    'site:.org (intext:"volunteer" OR "service" OR "humanitarian") (inurl:/shop OR inurl:/store) (intext:"authorize.net" OR intext:"authorizenet") -site:authorize.net'
]

# Dorks de Payflow organizados por categorías
PAYFLOW_DORKS = [
    # Plantas y jardinería
    '(inurl:/shop OR inurl:/store OR inurl:/product OR inurl:/checkout OR inurl:/cart) (intext:"payflow" OR intext:"payflowpro" OR intext:"paypal payflow" OR intext:"payflow gateway") (intext:"plant" OR "succulent" OR "cactus" OR "bonsai" OR "garden" OR "gardening" OR "nursery" OR "flower" OR "botanical" OR "houseplant" OR "terrarium" OR "fertilizer" OR "soil" OR "seeds") -site:paypal.com -site:github.com -site:reddit.com -site:facebook.com -site:twitter.com -site:linkedin.com -site:instagram.com -inurl:/docs -inurl:/developer -inurl:/partners -inurl:/plugins -inurl:/integration -intext:"payment gateway" -intext:"reseller" -intext:"accept payments for clients" -intitle:"API" -intitle:"Documentation" (site:.com OR site:.org) after:2023',

    # Ropa y moda
    '(inurl:/shop OR inurl:/store OR inurl:/product OR inurl:/checkout OR inurl:/cart) (intext:"payflow" OR intext:"payflowpro" OR intext:"paypal payflow" OR intext:"payflow gateway") (intext:"clothing" OR "fashion" OR "apparel" OR "t-shirt" OR "shoes" OR "sneakers" OR "streetwear") -site:paypal.com -site:github.com -site:reddit.com -site:facebook.com -site:twitter.com -site:linkedin.com -site:instagram.com -inurl:/docs -inurl:/developer -inurl:/partners -inurl:/plugins -inurl:/integration -intext:"payment gateway" -intext:"reseller" -intext:"accept payments for clients" -intitle:"API" -intitle:"Documentation" (site:.com OR site:.org) after:2023',

    # Tecnología y gadgets
    '(inurl:/shop OR inurl:/store OR inurl:/product OR inurl:/checkout OR inurl:/cart) (intext:"payflow" OR intext:"payflowpro" OR intext:"paypal payflow" OR intext:"payflow gateway") (intext:"electronics" OR "gadgets" OR "tech" OR "laptop" OR "phone" OR "charger" OR "smartwatch" OR "tablet" OR "device") -site:paypal.com -site:github.com -site:reddit.com -site:facebook.com -site:twitter.com -site:linkedin.com -site:instagram.com -inurl:/docs -inurl:/developer -inurl:/partners -inurl:/plugins -inurl:/integration -intext:"payment gateway" -intext:"reseller" -intext:"accept payments for clients" -intitle:"API" -intitle:"Documentation" (site:.com OR site:.org) after:2023',

    # Herramientas y construcción
    '(inurl:/shop OR inurl:/store OR inurl:/product OR inurl:/checkout OR inurl:/cart) (intext:"payflow" OR intext:"payflowpro" OR intext:"paypal payflow" OR intext:"payflow gateway") (intext:"tools" OR "tool" OR "drill" OR "saw" OR "hammer" OR "construction" OR "hardware" OR "power tools" OR "screwdriver" OR "wrench") -site:paypal.com -site:github.com -site:reddit.com -site:facebook.com -site:twitter.com -site:linkedin.com -site:instagram.com -inurl:/docs -inurl:/developer -inurl:/partners -inurl:/plugins -inurl:/integration -intext:"payment gateway" -intext:"reseller" -intext:"accept payments for clients" -intitle:"API" -intitle:"Documentation" (site:.com OR site:.org) after:2023',

    # Libros y educación
    '(inurl:/shop OR inurl:/store OR inurl:/product OR inurl:/checkout OR inurl:/cart) (intext:"payflow" OR intext:"payflowpro" OR intext:"paypal payflow" OR intext:"payflow gateway") (intext:"book" OR "books" OR "novel" OR "literature" OR "reading" OR "study" OR "learning" OR "course" OR "ebook") -site:paypal.com -site:github.com -site:reddit.com -site:facebook.com -site:twitter.com -site:linkedin.com -site:instagram.com -inurl:/docs -inurl:/developer -inurl:/partners -inurl:/plugins -inurl:/integration -intext:"payment gateway" -intext:"reseller" -intext:"accept payments for clients" -intitle:"API" -intitle:"Documentation" (site:.com OR site:.org) after:2023',

    # Mascotas
    '(inurl:/shop OR inurl:/store OR inurl:/product OR inurl:/checkout OR inurl:/cart) (intext:"payflow" OR intext:"payflowpro" OR intext:"paypal payflow" OR intext:"payflow gateway") (intext:"pet" OR "pets" OR "dog" OR "cat" OR "leash" OR "pet toy" OR "collar" OR "treats" OR "pet food") -site:paypal.com -site:github.com -site:reddit.com -site:facebook.com -site:twitter.com -site:linkedin.com -site:instagram.com -inurl:/docs -inurl:/developer -inurl:/partners -inurl:/plugins -inurl:/integration -intext:"payment gateway" -intext:"reseller" -intext:"accept payments for clients" -intitle:"API" -intitle:"Documentation" (site:.com OR site:.org) after:2023',

    # Comida y bebida
    '(inurl:/shop OR inurl:/store OR inurl:/product OR inurl:/checkout OR inurl:/cart) (intext:"payflow" OR intext:"payflowpro" OR intext:"paypal payflow" OR intext:"payflow gateway") (intext:"chocolate" OR "snack" OR "coffee" OR "tea" OR "organic" OR "vegan" OR "honey" OR "spice" OR "gourmet" OR "wine") -site:paypal.com -site:github.com -site:reddit.com -site:facebook.com -site:twitter.com -site:linkedin.com -site:instagram.com -inurl:/docs -inurl:/developer -inurl:/partners -inurl:/plugins -inurl:/integration -intext:"payment gateway" -intext:"reseller" -intext:"accept payments for clients" -intitle:"API" -intitle:"Documentation" (site:.com OR site:.org) after:2023',

    # Videojuegos y entretenimiento
    '(inurl:/shop OR inurl:/store OR inurl:/product OR inurl:/checkout OR inurl:/cart) (intext:"payflow" OR intext:"payflowpro" OR intext:"paypal payflow" OR intext:"payflow gateway") (intext:"gaming" OR "games" OR "gamepad" OR "console" OR "PC game" OR "video game" OR "playstation" OR "xbox") -site:paypal.com -site:github.com -site:reddit.com -site:facebook.com -site:twitter.com -site:linkedin.com -site:instagram.com -inurl:/docs -inurl:/developer -inurl:/partners -inurl:/plugins -inurl:/integration -intext:"payment gateway" -intext:"reseller" -intext:"accept payments for clients" -intitle:"API" -intitle:"Documentation" (site:.com OR site:.org) after:2023',

    # Arte, diseño y decoración
    '(inurl:/shop OR inurl:/store OR inurl:/product OR inurl:/checkout OR inurl:/cart) (intext:"payflow" OR intext:"payflowpro" OR intext:"paypal payflow" OR intext:"payflow gateway") (intext:"art" OR "prints" OR "canvas" OR "poster" OR "illustration" OR "decor" OR "home design" OR "interior") -site:paypal.com -site:github.com -site:reddit.com -site:facebook.com -site:twitter.com -site:linkedin.com -site:instagram.com -inurl:/docs -inurl:/developer -inurl:/partners -inurl:/plugins -inurl:/integration -intext:"payment gateway" -intext:"reseller" -intext:"accept payments for clients" -intitle:"API" -intitle:"Documentation" (site:.com OR site:.org) after:2023',

    # Joyas y accesorios
    '(inurl:/shop OR inurl:/store OR inurl:/product OR inurl:/checkout OR inurl:/cart) (intext:"payflow" OR intext:"payflowpro" OR intext:"paypal payflow" OR intext:"payflow gateway") (intext:"jewelry" OR "jewellery" OR "necklace" OR "ring" OR "bracelet" OR "earrings" OR "watch" OR "accessories") -site:paypal.com -site:github.com -site:reddit.com -site:facebook.com -site:twitter.com -site:linkedin.com -site:instagram.com -inurl:/docs -inurl:/developer -inurl:/partners -inurl:/plugins -inurl:/integration -intext:"payment gateway" -intext:"reseller" -intext:"accept payments for clients" -intitle:"API" -intitle:"Documentation" (site:.com OR site:.org) after:2023',

    # Deportes y fitness
    '(inurl:/shop OR inurl:/store OR inurl:/product OR inurl:/checkout OR inurl:/cart) (intext:"payflow" OR intext:"payflowpro" OR intext:"paypal payflow" OR intext:"payflow gateway") (intext:"sports" OR "fitness" OR "gym" OR "workout" OR "athletic" OR "running" OR "yoga" OR "exercise") -site:paypal.com -site:github.com -site:reddit.com -site:facebook.com -site:twitter.com -site:linkedin.com -site:instagram.com -inurl:/docs -inurl:/developer -inurl:/partners -inurl:/plugins -inurl:/integration -intext:"payment gateway" -intext:"reseller" -intext:"accept payments for clients" -intitle:"API" -intitle:"Documentation" (site:.com OR site:.org) after:2023',

    # Salud y belleza
    '(inurl:/shop OR inurl:/store OR inurl:/product OR inurl:/checkout OR inurl:/cart) (intext:"payflow" OR intext:"payflowpro" OR intext:"paypal payflow" OR intext:"payflow gateway") (intext:"beauty" OR "cosmetics" OR "skincare" OR "makeup" OR "health" OR "supplements" OR "vitamins") -site:paypal.com -site:github.com -site:reddit.com -site:facebook.com -site:twitter.com -site:linkedin.com -site:instagram.com -inurl:/docs -inurl:/developer -inurl:/partners -inurl:/plugins -inurl:/integration -intext:"payment gateway" -intext:"reseller" -intext:"accept payments for clients" -intitle:"API" -intitle:"Documentation" (site:.com OR site:.org) after:2023',

    # Automotriz
    '(inurl:/shop OR inurl:/store OR inurl:/product OR inurl:/checkout OR inurl:/cart) (intext:"payflow" OR intext:"payflowpro" OR intext:"paypal payflow" OR intext:"payflow gateway") (intext:"automotive" OR "car parts" OR "motorcycle" OR "auto accessories" OR "tires" OR "battery") -site:paypal.com -site:github.com -site:reddit.com -site:facebook.com -site:twitter.com -site:linkedin.com -site:instagram.com -inurl:/docs -inurl:/developer -inurl:/partners -inurl:/plugins -inurl:/integration -intext:"payment gateway" -intext:"reseller" -intext:"accept payments for clients" -intitle:"API" -intitle:"Documentation" (site:.com OR site:.org) after:2023',

    # Hogar y muebles
    '(inurl:/shop OR inurl:/store OR inurl:/product OR inurl:/checkout OR inurl:/cart) (intext:"payflow" OR intext:"payflowpro" OR intext:"paypal payflow" OR intext:"payflow gateway") (intext:"furniture" OR "home goods" OR "kitchen" OR "appliances" OR "bedding" OR "lighting") -site:paypal.com -site:github.com -site:reddit.com -site:facebook.com -site:twitter.com -site:linkedin.com -site:instagram.com -inurl:/docs -inurl:/developer -inurl:/partners -inurl:/plugins -inurl:/integration -intext:"payment gateway" -intext:"reseller" -intext:"accept payments for clients" -intitle:"API" -intitle:"Documentation" (site:.com OR site:.org) after:2023',

    # Música y instrumentos
    '(inurl:/shop OR inurl:/store OR inurl:/product OR inurl:/checkout OR inurl:/cart) (intext:"payflow" OR intext:"payflowpro" OR intext:"paypal payflow" OR intext:"payflow gateway") (intext:"music" OR "instruments" OR "guitar" OR "piano" OR "drums" OR "audio equipment") -site:paypal.com -site:github.com -site:reddit.com -site:facebook.com -site:twitter.com -site:linkedin.com -site:instagram.com -inurl:/docs -inurl:/developer -inurl:/partners -inurl:/plugins -inurl:/integration -intext:"payment gateway" -intext:"reseller" -intext:"accept payments for clients" -intitle:"API" -intitle:"Documentation" (site:.com OR site:.org) after:2023',

    # Bebés y niños
    '(inurl:/shop OR inurl:/store OR inurl:/product OR inurl:/checkout OR inurl:/cart) (intext:"payflow" OR intext:"payflowpro" OR intext:"paypal payflow" OR intext:"payflow gateway") (intext:"baby" OR "kids" OR "children" OR "toys" OR "stroller" OR "diapers" OR "nursery") -site:paypal.com -site:github.com -site:reddit.com -site:facebook.com -site:twitter.com -site:linkedin.com -site:instagram.com -inurl:/docs -inurl:/developer -inurl:/partners -inurl:/plugins -inurl:/integration -intext:"payment gateway" -intext:"reseller" -intext:"accept payments for clients" -intitle:"API" -intitle:"Documentation" (site:.com OR site:.org) after:2023',

    # Outdoor y camping
    '(inurl:/shop OR inurl:/store OR inurl:/product OR inurl:/checkout OR inurl:/cart) (intext:"payflow" OR intext:"payflowpro" OR intext:"paypal payflow" OR intext:"payflow gateway") (intext:"outdoor" OR "camping" OR "hiking" OR "fishing" OR "hunting" OR "survival gear") -site:paypal.com -site:github.com -site:reddit.com -site:facebook.com -site:twitter.com -site:linkedin.com -site:instagram.com -inurl:/docs -inurl:/developer -inurl:/partners -inurl:/plugins -inurl:/integration -intext:"payment gateway" -intext:"reseller" -intext:"accept payments for clients" -intitle:"API" -intitle:"Documentation" (site:.com OR site:.org) after:2023',

    # Oficina y papelería
    '(inurl:/shop OR inurl:/store OR inurl:/product OR inurl:/checkout OR inurl:/cart) (intext:"payflow" OR intext:"payflowpro" OR intext:"paypal payflow" OR intext:"payflow gateway") (intext:"office supplies" OR "stationery" OR "printer" OR "desk" OR "chair" OR "notebook") -site:paypal.com -site:github.com -site:reddit.com -site:facebook.com -site:twitter.com -site:linkedin.com -site:instagram.com -inurl:/docs -inurl:/developer -inurl:/partners -inurl:/plugins -inurl:/integration -intext:"payment gateway" -intext:"reseller" -intext:"accept payments for clients" -intitle:"API" -intitle:"Documentation" (site:.com OR site:.org) after:2023',

    # Dorks genéricos adicionales
    '(inurl:/shop OR inurl:/store OR inurl:/product OR inurl:/checkout OR inurl:/cart) (intext:"payflow" OR intext:"payflowpro" OR intext:"paypal payflow" OR intext:"payflow gateway") -site:paypal.com -site:github.com -site:reddit.com -site:facebook.com -site:twitter.com -site:linkedin.com -site:instagram.com -inurl:/docs -inurl:/developer -inurl:/partners -inurl:/plugins -inurl:/integration -intext:"payment gateway" -intext:"reseller" -intext:"accept payments for clients" -intitle:"API" -intitle:"Documentation" (site:.com OR site:.org) after:2023',

    # Dorks específicos para sitios .org - Organizaciones y tiendas
    'site:.org (inurl:/shop OR inurl:/store OR inurl:/checkout) (intext:"payflow" OR intext:"payflowpro") (intext:"nonprofit" OR "charity" OR "foundation") -site:paypal.com -site:github.com',
    'site:.org (inurl:/donate OR inurl:/donation OR inurl:/give) (intext:"payflow" OR intext:"payflowpro") -site:paypal.com -site:github.com',
    'site:.org (inurl:/merchandise OR inurl:/merch OR inurl:/gift) (intext:"payflow" OR intext:"payflowpro") -site:paypal.com -site:github.com',
    'site:.org (intext:"museum store" OR "museum shop") (intext:"payflow" OR intext:"payflowpro") -site:paypal.com -site:github.com',
    'site:.org (intext:"university store" OR "college store") (intext:"payflow" OR intext:"payflowpro") -site:paypal.com -site:github.com',
    'site:.org (intext:"church store" OR "religious store") (intext:"payflow" OR intext:"payflowpro") -site:paypal.com -site:github.com',
    'site:.org (intext:"wildlife" OR "conservation" OR "environment") (inurl:/shop OR inurl:/store) (intext:"payflow" OR intext:"payflowpro") -site:paypal.com',
    'site:.org (intext:"art gallery" OR "artist" OR "craft") (inurl:/shop OR inurl:/store) (intext:"payflow" OR intext:"payflowpro") -site:paypal.com',
    'site:.org (intext:"community" OR "local" OR "neighborhood") (inurl:/shop OR inurl:/store) (intext:"payflow" OR intext:"payflowpro") -site:paypal.com',
    'site:.org (intext:"health" OR "medical" OR "wellness") (inurl:/shop OR inurl:/store) (intext:"payflow" OR intext:"payflowpro") -site:paypal.com',
    'site:.org (intext:"education" OR "school" OR "learning") (inurl:/shop OR inurl:/store) (intext:"payflow" OR intext:"payflowpro") -site:paypal.com',
    'site:.org (intext:"sports club" OR "athletic" OR "team") (inurl:/shop OR inurl:/store) (intext:"payflow" OR intext:"payflowpro") -site:paypal.com',
    'site:.org (intext:"library" OR "book" OR "reading") (inurl:/shop OR inurl:/store) (intext:"payflow" OR intext:"payflowpro") -site:paypal.com',
    'site:.org (intext:"festival" OR "event" OR "conference") (inurl:/shop OR inurl:/store OR inurl:/ticket) (intext:"payflow" OR intext:"payflowpro") -site:paypal.com',
    'site:.org (intext:"volunteer" OR "service" OR "humanitarian") (inurl:/shop OR inurl:/store) (intext:"payflow" OR intext:"payflowpro") -site:paypal.com'
]

# Dorks de Adyen organizados por categorías
ADYEN_DORKS = [
    # Plantas y jardinería
    '(inurl:/shop OR inurl:/store OR inurl:/product OR inurl:/checkout OR inurl:/cart) (intext:"adyen" OR intext:"adyen.com" OR intext:"adyenpayments" OR intext:"adyen payments") (intext:"plant" OR "succulent" OR "cactus" OR "bonsai" OR "garden" OR "gardening" OR "nursery" OR "flower" OR "botanical" OR "houseplant" OR "terrarium" OR "fertilizer" OR "soil" OR "seeds") -site:adyen.com -site:github.com -site:reddit.com -site:facebook.com -site:twitter.com -site:linkedin.com -site:instagram.com -inurl:/docs -inurl:/developer -inurl:/partners -inurl:/plugins -inurl:/integration -intext:"payment gateway" -intext:"reseller" -intext:"accept payments for clients" -intitle:"API" -intitle:"Documentation" (site:.com OR site:.org) after:2023',

    # Ropa y moda
    '(inurl:/shop OR inurl:/store OR inurl:/product OR inurl:/checkout OR inurl:/cart) (intext:"adyen" OR intext:"adyen.com" OR intext:"adyenpayments" OR intext:"adyen payments") (intext:"clothing" OR "fashion" OR "apparel" OR "t-shirt" OR "shoes" OR "sneakers" OR "streetwear") -site:adyen.com -site:github.com -site:reddit.com -site:facebook.com -site:twitter.com -site:linkedin.com -site:instagram.com -inurl:/docs -inurl:/developer -inurl:/partners -inurl:/plugins -inurl:/integration -intext:"payment gateway" -intext:"reseller" -intext:"accept payments for clients" -intitle:"API" -intitle:"Documentation" (site:.com OR site:.org) after:2023',

    # Tecnología y gadgets
    '(inurl:/shop OR inurl:/store OR inurl:/product OR inurl:/checkout OR inurl:/cart) (intext:"adyen" OR intext:"adyen.com" OR intext:"adyenpayments" OR intext:"adyen payments") (intext:"electronics" OR "gadgets" OR "tech" OR "laptop" OR "phone" OR "charger" OR "smartwatch" OR "tablet" OR "device") -site:adyen.com -site:github.com -site:reddit.com -site:facebook.com -site:twitter.com -site:linkedin.com -site:instagram.com -inurl:/docs -inurl:/developer -inurl:/partners -inurl:/plugins -inurl:/integration -intext:"payment gateway" -intext:"reseller" -intext:"accept payments for clients" -intitle:"API" -intitle:"Documentation" (site:.com OR site:.org) after:2023',

    # Herramientas y construcción
    '(inurl:/shop OR inurl:/store OR inurl:/product OR inurl:/checkout OR inurl:/cart) (intext:"adyen" OR intext:"adyen.com" OR intext:"adyenpayments" OR intext:"adyen payments") (intext:"tools" OR "tool" OR "drill" OR "saw" OR "hammer" OR "construction" OR "hardware" OR "power tools" OR "screwdriver" OR "wrench") -site:adyen.com -site:github.com -site:reddit.com -site:facebook.com -site:twitter.com -site:linkedin.com -site:instagram.com -inurl:/docs -inurl:/developer -inurl:/partners -inurl:/plugins -inurl:/integration -intext:"payment gateway" -intext:"reseller" -intext:"accept payments for clients" -intitle:"API" -intitle:"Documentation" (site:.com OR site:.org) after:2023',

    # Libros y educación
    '(inurl:/shop OR inurl:/store OR inurl:/product OR inurl:/checkout OR inurl:/cart) (intext:"adyen" OR intext:"adyen.com" OR intext:"adyenpayments" OR intext:"adyen payments") (intext:"book" OR "books" OR "novel" OR "literature" OR "reading" OR "study" OR "learning" OR "course" OR "ebook") -site:adyen.com -site:github.com -site:reddit.com -site:facebook.com -site:twitter.com -site:linkedin.com -site:instagram.com -inurl:/docs -inurl:/developer -inurl:/partners -inurl:/plugins -inurl:/integration -intext:"payment gateway" -intext:"reseller" -intext:"accept payments for clients" -intitle:"API" -intitle:"Documentation" (site:.com OR site:.org) after:2023',

    # Mascotas
    '(inurl:/shop OR inurl:/store OR inurl:/product OR inurl:/checkout OR inurl:/cart) (intext:"adyen" OR intext:"adyen.com" OR intext:"adyenpayments" OR intext:"adyen payments") (intext:"pet" OR "pets" OR "dog" OR "cat" OR "leash" OR "pet toy" OR "collar" OR "treats" OR "pet food") -site:adyen.com -site:github.com -site:reddit.com -site:facebook.com -site:twitter.com -site:linkedin.com -site:instagram.com -inurl:/docs -inurl:/developer -inurl:/partners -inurl:/plugins -inurl:/integration -intext:"payment gateway" -intext:"reseller" -intext:"accept payments for clients" -intitle:"API" -intitle:"Documentation" (site:.com OR site:.org) after:2023',

    # Comida y bebida
    '(inurl:/shop OR inurl:/store OR inurl:/product OR inurl:/checkout OR inurl:/cart) (intext:"adyen" OR intext:"adyen.com" OR intext:"adyenpayments" OR intext:"adyen payments") (intext:"chocolate" OR "snack" OR "coffee" OR "tea" OR "organic" OR "vegan" OR "honey" OR "spice" OR "gourmet" OR "wine") -site:adyen.com -site:github.com -site:reddit.com -site:facebook.com -site:twitter.com -site:linkedin.com -site:instagram.com -inurl:/docs -inurl:/developer -inurl:/partners -inurl:/plugins -inurl:/integration -intext:"payment gateway" -intext:"reseller" -intext:"accept payments for clients" -intitle:"API" -intitle:"Documentation" (site:.com OR site:.org) after:2023',

    # Videojuegos y entretenimiento
    '(inurl:/shop OR inurl:/store OR inurl:/product OR inurl:/checkout OR inurl:/cart) (intext:"adyen" OR intext:"adyen.com" OR intext:"adyenpayments" OR intext:"adyen payments") (intext:"gaming" OR "games" OR "gamepad" OR "console" OR "PC game" OR "video game" OR "playstation" OR "xbox") -site:adyen.com -site:github.com -site:reddit.com -site:facebook.com -site:twitter.com -site:linkedin.com -site:instagram.com -inurl:/docs -inurl:/developer -inurl:/partners -inurl:/plugins -inurl:/integration -intext:"payment gateway" -intext:"reseller" -intext:"accept payments for clients" -intitle:"API" -intitle:"Documentation" (site:.com OR site:.org) after:2023',

    # Arte, diseño y decoración
    '(inurl:/shop OR inurl:/store OR inurl:/product OR inurl:/checkout OR inurl:/cart) (intext:"adyen" OR intext:"adyen.com" OR intext:"adyenpayments" OR intext:"adyen payments") (intext:"art" OR "prints" OR "canvas" OR "poster" OR "illustration" OR "decor" OR "home design" OR "interior") -site:adyen.com -site:github.com -site:reddit.com -site:facebook.com -site:twitter.com -site:linkedin.com -site:instagram.com -inurl:/docs -inurl:/developer -inurl:/partners -inurl:/plugins -inurl:/integration -intext:"payment gateway" -intext:"reseller" -intext:"accept payments for clients" -intitle:"API" -intitle:"Documentation" (site:.com OR site:.org) after:2023',

    # Joyas y accesorios
    '(inurl:/shop OR inurl:/store OR inurl:/product OR inurl:/checkout OR inurl:/cart) (intext:"adyen" OR intext:"adyen.com" OR intext:"adyenpayments" OR intext:"adyen payments") (intext:"jewelry" OR "jewellery" OR "necklace" OR "ring" OR "bracelet" OR "earrings" OR "watch" OR "accessories") -site:adyen.com -site:github.com -site:reddit.com -site:facebook.com -site:twitter.com -site:linkedin.com -site:instagram.com -inurl:/docs -inurl:/developer -inurl:/partners -inurl:/plugins -inurl:/integration -intext:"payment gateway" -intext:"reseller" -intext:"accept payments for clients" -intitle:"API" -intitle:"Documentation" (site:.com OR site:.org) after:2023',

    # Deportes y fitness
    '(inurl:/shop OR inurl:/store OR inurl:/product OR inurl:/checkout OR inurl:/cart) (intext:"adyen" OR intext:"adyen.com" OR intext:"adyenpayments" OR intext:"adyen payments") (intext:"sports" OR "fitness" OR "gym" OR "workout" OR "athletic" OR "running" OR "yoga" OR "exercise") -site:adyen.com -site:github.com -site:reddit.com -site:facebook.com -site:twitter.com -site:linkedin.com -site:instagram.com -inurl:/docs -inurl:/developer -inurl:/partners -inurl:/plugins -inurl:/integration -intext:"payment gateway" -intext:"reseller" -intext:"accept payments for clients" -intitle:"API" -intitle:"Documentation" (site:.com OR site:.org) after:2023',

    # Salud y belleza
    '(inurl:/shop OR inurl:/store OR inurl:/product OR inurl:/checkout OR inurl:/cart) (intext:"adyen" OR intext:"adyen.com" OR intext:"adyenpayments" OR intext:"adyen payments") (intext:"beauty" OR "cosmetics" OR "skincare" OR "makeup" OR "health" OR "supplements" OR "vitamins") -site:adyen.com -site:github.com -site:reddit.com -site:facebook.com -site:twitter.com -site:linkedin.com -site:instagram.com -inurl:/docs -inurl:/developer -inurl:/partners -inurl:/plugins -inurl:/integration -intext:"payment gateway" -intext:"reseller" -intext:"accept payments for clients" -intitle:"API" -intitle:"Documentation" (site:.com OR site:.org) after:2023',

    # Automotriz
    '(inurl:/shop OR inurl:/store OR inurl:/product OR inurl:/checkout OR inurl:/cart) (intext:"adyen" OR intext:"adyen.com" OR intext:"adyenpayments" OR intext:"adyen payments") (intext:"automotive" OR "car parts" OR "motorcycle" OR "auto accessories" OR "tires" OR "battery") -site:adyen.com -site:github.com -site:reddit.com -site:facebook.com -site:twitter.com -site:linkedin.com -site:instagram.com -inurl:/docs -inurl:/developer -inurl:/partners -inurl:/plugins -inurl:/integration -intext:"payment gateway" -intext:"reseller" -intext:"accept payments for clients" -intitle:"API" -intitle:"Documentation" (site:.com OR site:.org) after:2023',

    # Hogar y muebles
    '(inurl:/shop OR inurl:/store OR inurl:/product OR inurl:/checkout OR inurl:/cart) (intext:"adyen" OR intext:"adyen.com" OR intext:"adyenpayments" OR intext:"adyen payments") (intext:"furniture" OR "home goods" OR "kitchen" OR "appliances" OR "bedding" OR "lighting") -site:adyen.com -site:github.com -site:reddit.com -site:facebook.com -site:twitter.com -site:linkedin.com -site:instagram.com -inurl:/docs -inurl:/developer -inurl:/partners -inurl:/plugins -inurl:/integration -intext:"payment gateway" -intext:"reseller" -intext:"accept payments for clients" -intitle:"API" -intitle:"Documentation" (site:.com OR site:.org) after:2023',

    # Música y instrumentos
    '(inurl:/shop OR inurl:/store OR inurl:/product OR inurl:/checkout OR inurl:/cart) (intext:"adyen" OR intext:"adyen.com" OR intext:"adyenpayments" OR intext:"adyen payments") (intext:"music" OR "instruments" OR "guitar" OR "piano" OR "drums" OR "audio equipment") -site:adyen.com -site:github.com -site:reddit.com -site:facebook.com -site:twitter.com -site:linkedin.com -site:instagram.com -inurl:/docs -inurl:/developer -inurl:/partners -inurl:/plugins -inurl:/integration -intext:"payment gateway" -intext:"reseller" -intext:"accept payments for clients" -intitle:"API" -intitle:"Documentation" (site:.com OR site:.org) after:2023',

    # Bebés y niños
    '(inurl:/shop OR inurl:/store OR inurl:/product OR inurl:/checkout OR inurl:/cart) (intext:"adyen" OR intext:"adyen.com" OR intext:"adyenpayments" OR intext:"adyen payments") (intext:"baby" OR "kids" OR "children" OR "toys" OR "stroller" OR "diapers" OR "nursery") -site:adyen.com -site:github.com -site:reddit.com -site:facebook.com -site:twitter.com -site:linkedin.com -site:instagram.com -inurl:/docs -inurl:/developer -inurl:/partners -inurl:/plugins -inurl:/integration -intext:"payment gateway" -intext:"reseller" -intext:"accept payments for clients" -intitle:"API" -intitle:"Documentation" (site:.com OR site:.org) after:2023',

    # Outdoor y camping
    '(inurl:/shop OR inurl:/store OR inurl:/product OR inurl:/checkout OR inurl:/cart) (intext:"adyen" OR intext:"adyen.com" OR intext:"adyenpayments" OR intext:"adyen payments") (intext:"outdoor" OR "camping" OR "hiking" OR "fishing" OR "hunting" OR "survival gear") -site:adyen.com -site:github.com -site:reddit.com -site:facebook.com -site:twitter.com -site:linkedin.com -site:instagram.com -inurl:/docs -inurl:/developer -inurl:/partners -inurl:/plugins -inurl:/integration -intext:"payment gateway" -intext:"reseller" -intext:"accept payments for clients" -intitle:"API" -intitle:"Documentation" (site:.com OR site:.org) after:2023',

    # Oficina y papelería
    '(inurl:/shop OR inurl:/store OR inurl:/product OR inurl:/checkout OR inurl:/cart) (intext:"adyen" OR intext:"adyen.com" OR intext:"adyenpayments" OR intext:"adyen payments") (intext:"office supplies" OR "stationery" OR "printer" OR "desk" OR "chair" OR "notebook") -site:adyen.com -site:github.com -site:reddit.com -site:facebook.com -site:twitter.com -site:linkedin.com -site:instagram.com -inurl:/docs -inurl:/developer -inurl:/partners -inurl:/plugins -inurl:/integration -intext:"payment gateway" -intext:"reseller" -intext:"accept payments for clients" -intitle:"API" -intitle:"Documentation" (site:.com OR site:.org) after:2023',

    # Dorks genéricos adicionales
    '(inurl:/shop OR inurl:/store OR inurl:/product OR inurl:/checkout OR inurl:/cart) (intext:"adyen" OR intext:"adyen.com" OR intext:"adyenpayments" OR intext:"adyen payments") -site:adyen.com -site:github.com -site:reddit.com -site:facebook.com -site:twitter.com -site:linkedin.com -site:instagram.com -inurl:/docs -inurl:/developer -inurl:/partners -inurl:/plugins -inurl:/integration -intext:"payment gateway" -intext:"reseller" -intext:"accept payments for clients" -intitle:"API" -intitle:"Documentation" (site:.com OR site:.org) after:2023',

    # Dorks específicos para sitios .org - Organizaciones y tiendas
    'site:.org (inurl:/shop OR inurl:/store OR inurl:/checkout) (intext:"adyen" OR intext:"adyenpayments") (intext:"nonprofit" OR "charity" OR "foundation") -site:adyen.com -site:github.com',
    'site:.org (inurl:/donate OR inurl:/donation OR inurl:/give) (intext:"adyen" OR intext:"adyenpayments") -site:adyen.com -site:github.com',
    'site:.org (inurl:/merchandise OR inurl:/merch OR inurl:/gift) (intext:"adyen" OR intext:"adyenpayments") -site:adyen.com -site:github.com',
    'site:.org (intext:"museum store" OR "museum shop") (intext:"adyen" OR intext:"adyenpayments") -site:adyen.com -site:github.com',
    'site:.org (intext:"university store" OR "college store") (intext:"adyen" OR intext:"adyenpayments") -site:adyen.com -site:github.com',
    'site:.org (intext:"church store" OR "religious store") (intext:"adyen" OR intext:"adyenpayments") -site:adyen.com -site:github.com',
    'site:.org (intext:"wildlife" OR "conservation" OR "environment") (inurl:/shop OR inurl:/store) (intext:"adyen" OR intext:"adyenpayments") -site:adyen.com',
    'site:.org (intext:"art gallery" OR "artist" OR "craft") (inurl:/shop OR inurl:/store) (intext:"adyen" OR intext:"adyenpayments") -site:adyen.com',
    'site:.org (intext:"community" OR "local" OR "neighborhood") (inurl:/shop OR inurl:/store) (intext:"adyen" OR intext:"adyenpayments") -site:adyen.com',
    'site:.org (intext:"health" OR "medical" OR "wellness") (inurl:/shop OR inurl:/store) (intext:"adyen" OR intext:"adyenpayments") -site:adyen.com',
    'site:.org (intext:"education" OR "school" OR "learning") (inurl:/shop OR inurl:/store) (intext:"adyen" OR intext:"adyenpayments") -site:adyen.com',
    'site:.org (intext:"sports club" OR "athletic" OR "team") (inurl:/shop OR inurl:/store) (intext:"adyen" OR intext:"adyenpayments") -site:adyen.com',
    'site:.org (intext:"library" OR "book" OR "reading") (inurl:/shop OR inurl:/store) (intext:"adyen" OR intext:"adyenpayments") -site:adyen.com',
    'site:.org (intext:"festival" OR "event" OR "conference") (inurl:/shop OR inurl:/store OR inurl:/ticket) (intext:"adyen" OR intext:"adyenpayments") -site:adyen.com',
    'site:.org (intext:"volunteer" OR "service" OR "humanitarian") (inurl:/shop OR inurl:/store) (intext:"adyen" OR intext:"adyenpayments") -site:adyen.com'
]

# Dorks de Worldpay organizados por categorías - EXPANDIDO
WORLDPAY_DORKS = [
    # Plantas y jardinería
    '(inurl:/shop OR inurl:/store OR inurl:/product OR inurl:/checkout OR inurl:/cart) (intext:"worldpay" OR intext:"worldpay.com" OR intext:"worldpay.js" OR intext:"worldpay payments") (intext:"plant" OR "succulent" OR "cactus" OR "bonsai" OR "garden" OR "gardening" OR "nursery" OR "flower" OR "botanical" OR "houseplant" OR "terrarium" OR "fertilizer" OR "soil" OR "seeds" OR "greenhouse" OR "landscaping" OR "irrigation" OR "pruning" OR "compost" OR "mulch") -site:worldpay.com -site:github.com -site:reddit.com -site:facebook.com -site:twitter.com -site:linkedin.com -site:instagram.com -inurl:/docs -inurl:/developer -inurl:/partners -inurl:/plugins -inurl:/integration -intext:"payment gateway" -intext:"reseller" -intext:"accept payments for clients" -intitle:"API" -intitle:"Documentation" (site:.com OR site:.org) after:2023',

    # Ropa y moda
    '(inurl:/shop OR inurl:/store OR inurl:/product OR inurl:/checkout OR inurl:/cart) (intext:"worldpay" OR intext:"worldpay.com" OR intext:"worldpay.js" OR intext:"worldpay payments") (intext:"clothing" OR "fashion" OR "apparel" OR "t-shirt" OR "shoes" OR "sneakers" OR "streetwear" OR "dress" OR "jeans" OR "jacket" OR "coat" OR "hoodie" OR "pants" OR "shorts" OR "underwear" OR "socks" OR "hat" OR "cap" OR "scarf" OR "gloves" OR "belt" OR "handbag" OR "purse" OR "wallet") -site:worldpay.com -site:github.com -site:reddit.com -site:facebook.com -site:twitter.com -site:linkedin.com -site:instagram.com -inurl:/docs -inurl:/developer -inurl:/partners -inurl:/plugins -inurl:/integration -intext:"payment gateway" -intext:"reseller" -intext:"accept payments for clients" -intitle:"API" -intitle:"Documentation" (site:.com OR site:.org) after:2023',

    # Tecnología y gadgets
    '(inurl:/shop OR inurl:/store OR inurl:/product OR inurl:/checkout OR inurl:/cart) (intext:"worldpay" OR intext:"worldpay.com" OR intext:"worldpay.js" OR intext:"worldpay payments") (intext:"electronics" OR "gadgets" OR "tech" OR "laptop" OR "phone" OR "charger" OR "smartwatch" OR "tablet" OR "device" OR "computer" OR "mouse" OR "keyboard" OR "headphones" OR "speaker" OR "camera" OR "drone" OR "VR" OR "AR" OR "smart home" OR "IoT") -site:worldpay.com -site:github.com -site:reddit.com -site:facebook.com -site:twitter.com -site:linkedin.com -site:instagram.com -inurl:/docs -inurl:/developer -inurl:/partners -inurl:/plugins -inurl:/integration -intext:"payment gateway" -intext:"reseller" -intext:"accept payments for clients" -intitle:"API" -intitle:"Documentation" (site:.com OR site:.org) after:2023',

    # Herramientas y construcción
    '(inurl:/shop OR inurl:/store OR inurl:/product OR inurl:/checkout OR inurl:/cart) (intext:"worldpay" OR intext:"worldpay.com" OR intext:"worldpay.js" OR intext:"worldpay payments") (intext:"tools" OR "tool" OR "drill" OR "saw" OR "hammer" OR "construction" OR "hardware" OR "power tools" OR "screwdriver" OR "wrench" OR "plumbing" OR "electrical" OR "safety" OR "measuring" OR "welding" OR "woodworking" OR "metalworking" OR "pliers") -site:worldpay.com -site:github.com -site:reddit.com -site:facebook.com -site:twitter.com -site:linkedin.com -site:instagram.com -inurl:/docs -inurl:/developer -inurl:/partners -inurl:/plugins -inurl:/integration -intext:"payment gateway" -intext:"reseller" -intext:"accept payments for clients" -intitle:"API" -intitle:"Documentation" (site:.com OR site:.org) after:2023',

    # Libros y educación
    '(inurl:/shop OR inurl:/store OR inurl:/product OR inurl:/checkout OR inurl:/cart) (intext:"worldpay" OR intext:"worldpay.com" OR intext:"worldpay.js" OR intext:"worldpay payments") (intext:"book" OR "books" OR "novel" OR "literature" OR "reading" OR "study" OR "learning" OR "course" OR "ebook" OR "textbook" OR "magazine" OR "journal" OR "encyclopedia" OR "dictionary" OR "biography" OR "fiction" OR "academic" OR "research") -site:worldpay.com -site:github.com -site:reddit.com -site:facebook.com -site:twitter.com -site:linkedin.com -site:instagram.com -inurl:/docs -inurl:/developer -inurl:/partners -inurl:/plugins -inurl:/integration -intext:"payment gateway" -intext:"reseller" -intext:"accept payments for clients" -intitle:"API" -intitle:"Documentation" (site:.com OR site:.org) after:2023',

    # Mascotas y animales
    '(inurl:/shop OR inurl:/store OR inurl:/product OR inurl:/checkout OR inurl:/cart) (intext:"worldpay" OR intext:"worldpay.com" OR intext:"worldpay.js" OR intext:"worldpay payments") (intext:"pet" OR "pets" OR "dog" OR "cat" OR "leash" OR "pet toy" OR "collar" OR "treats" OR "pet food" OR "aquarium" OR "bird" OR "reptile" OR "hamster" OR "rabbit" OR "fish" OR "grooming" OR "veterinary" OR "animal" OR "supplies") -site:worldpay.com -site:github.com -site:reddit.com -site:facebook.com -site:twitter.com -site:linkedin.com -site:instagram.com -inurl:/docs -inurl:/developer -inurl:/partners -inurl:/plugins -inurl:/integration -intext:"payment gateway" -intext:"reseller" -intext:"accept payments for clients" -intitle:"API" -intitle:"Documentation" (site:.com OR site:.org) after:2023',

    # Comida y bebida gourmet
    '(inurl:/shop OR inurl:/store OR inurl:/product OR inurl:/checkout OR inurl:/cart) (intext:"worldpay" OR intext:"worldpay.com" OR intext:"worldpay.js" OR intext:"worldpay payments") (intext:"chocolate" OR "snack" OR "coffee" OR "tea" OR "organic" OR "vegan" OR "honey" OR "spice" OR "gourmet" OR "wine" OR "beer" OR "whiskey" OR "vodka" OR "rum" OR "gin" OR "brandy" OR "champagne" OR "spirits" OR "artisan" OR "delicatessen") -site:worldpay.com -site:github.com -site:reddit.com -site:facebook.com -site:twitter.com -site:linkedin.com -site:instagram.com -inurl:/docs -inurl:/developer -inurl:/partners -inurl:/plugins -inurl:/integration -intext:"payment gateway" -intext:"reseller" -intext:"accept payments for clients" -intitle:"API" -intitle:"Documentation" (site:.com OR site:.org) after:2023',

    # Gaming y entretenimiento
    '(inurl:/shop OR inurl:/store OR inurl:/product OR inurl:/checkout OR inurl:/cart) (intext:"worldpay" OR intext:"worldpay.com" OR intext:"worldpay.js" OR intext:"worldpay payments") (intext:"gaming" OR "games" OR "gamepad" OR "console" OR "PC game" OR "video game" OR "playstation" OR "xbox" OR "nintendo" OR "steam" OR "board game" OR "card game" OR "puzzle" OR "toy" OR "collectible" OR "figure" OR "model" OR "arcade" OR "retro") -site:worldpay.com -site:github.com -site:reddit.com -site:facebook.com -site:twitter.com -site:linkedin.com -site:instagram.com -inurl:/docs -inurl:/developer -inurl:/partners -inurl:/plugins -inurl:/integration -intext:"payment gateway" -intext:"reseller" -intext:"accept payments for clients" -intitle:"API" -intitle:"Documentation" (site:.com OR site:.org) after:2023',

    # Arte y creatividad
    '(inurl:/shop OR inurl:/store OR inurl:/product OR inurl:/checkout OR inurl:/cart) (intext:"worldpay" OR intext:"worldpay.com" OR intext:"worldpay.js" OR intext:"worldpay payments") (intext:"art" OR "prints" OR "canvas" OR "poster" OR "illustration" OR "decor" OR "home design" OR "interior" OR "painting" OR "sculpture" OR "photography" OR "frame" OR "wall art" OR "handmade" OR "craft" OR "ceramic" OR "pottery" OR "vintage" OR "antique" OR "gallery") -site:worldpay.com -site:github.com -site:reddit.com -site:facebook.com -site:twitter.com -site:linkedin.com -site:instagram.com -inurl:/docs -inurl:/developer -inurl:/partners -inurl:/plugins -inurl:/integration -intext:"payment gateway" -intext:"reseller" -intext:"accept payments for clients" -intitle:"API" -intitle:"Documentation" (site:.com OR site:.org) after:2023',

    # Joyería y lujo
    '(inurl:/shop OR inurl:/store OR inurl:/product OR inurl:/checkout OR inurl:/cart) (intext:"worldpay" OR intext:"worldpay.com" OR intext:"worldpay.js" OR intext:"worldpay payments") (intext:"jewelry" OR "jewellery" OR "necklace" OR "ring" OR "bracelet" OR "earrings" OR "watch" OR "accessories" OR "diamond" OR "gold" OR "silver" OR "platinum" OR "pearl" OR "gemstone" OR "luxury" OR "designer" OR "precious" OR "fine jewelry") -site:worldpay.com -site:github.com -site:reddit.com -site:facebook.com -site:twitter.com -site:linkedin.com -site:instagram.com -inurl:/docs -inurl:/developer -inurl:/partners -inurl:/plugins -inurl:/integration -intext:"payment gateway" -intext:"reseller" -intext:"accept payments for clients" -intitle:"API" -intitle:"Documentation" (site:.com OR site:.org) after:2023',

    # Deportes y fitness avanzado
    '(inurl:/shop OR inurl:/store OR inurl:/product OR inurl:/checkout OR inurl:/cart) (intext:"worldpay" OR intext:"worldpay.com" OR intext:"worldpay.js" OR intext:"worldpay payments") (intext:"sports" OR "fitness" OR "gym" OR "workout" OR "athletic" OR "running" OR "yoga" OR "exercise" OR "weights" OR "dumbbells" OR "treadmill" OR "bike" OR "bicycle" OR "skateboard" OR "surfboard" OR "skiing" OR "snowboard" OR "martial arts" OR "boxing" OR "crossfit") -site:worldpay.com -site:github.com -site:reddit.com -site:facebook.com -site:twitter.com -site:linkedin.com -site:instagram.com -inurl:/docs -inurl:/developer -inurl:/partners -inurl:/plugins -inurl:/integration -intext:"payment gateway" -intext:"reseller" -intext:"accept payments for clients" -intitle:"API" -intitle:"Documentation" (site:.com OR site:.org) after:2023',

    # Salud y bienestar
    '(inurl:/shop OR inurl:/store OR inurl:/product OR inurl:/checkout OR inurl:/cart) (intext:"worldpay" OR intext:"worldpay.com" OR intext:"worldpay.js" OR intext:"worldpay payments") (intext:"beauty" OR "cosmetics" OR "skincare" OR "makeup" OR "health" OR "supplements" OR "vitamins" OR "wellness" OR "natural" OR "herbal" OR "aromatherapy" OR "essential oils" OR "spa" OR "massage" OR "meditation" OR "mindfulness") -site:worldpay.com -site:github.com -site:reddit.com -site:facebook.com -site:twitter.com -site:linkedin.com -site:instagram.com -inurl:/docs -inurl:/developer -inurl:/partners -inurl:/plugins -inurl:/integration -intext:"payment gateway" -intext:"reseller" -intext:"accept payments for clients" -intitle:"API" -intitle:"Documentation" (site:.com OR site:.org) after:2023',

    # Automotriz especializado
    '(inurl:/shop OR inurl:/store OR inurl:/product OR inurl:/checkout OR inurl:/cart) (intext:"worldpay" OR intext:"worldpay.com" OR intext:"worldpay.js" OR intext:"worldpay payments") (intext:"automotive" OR "car parts" OR "motorcycle" OR "auto accessories" OR "tires" OR "battery" OR "engine" OR "brake" OR "performance" OR "racing" OR "classic car" OR "restoration" OR "mechanic" OR "garage" OR "workshop") -site:worldpay.com -site:github.com -site:reddit.com -site:facebook.com -site:twitter.com -site:linkedin.com -site:instagram.com -inurl:/docs -inurl:/developer -inurl:/partners -inurl:/plugins -inurl:/integration -intext:"payment gateway" -intext:"reseller" -intext:"accept payments for clients" -intitle:"API" -intitle:"Documentation" (site:.com OR site:.org) after:2023',

    # Hogar y lifestyle
    '(inurl:/shop OR inurl:/store OR inurl:/product OR inurl:/checkout OR inurl:/cart) (intext:"worldpay" OR intext:"worldpay.com" OR intext:"worldpay.js" OR intext:"worldpay payments") (intext:"furniture" OR "home goods" OR "kitchen" OR "appliances" OR "bedding" OR "lighting" OR "bathroom" OR "garden furniture" OR "outdoor furniture" OR "smart home" OR "organization" OR "storage" OR "decor" OR "renovation" OR "improvement") -site:worldpay.com -site:github.com -site:reddit.com -site:facebook.com -site:twitter.com -site:linkedin.com -site:instagram.com -inurl:/docs -inurl:/developer -inurl:/partners -inurl:/plugins -inurl:/integration -intext:"payment gateway" -intext:"reseller" -intext:"accept payments for clients" -intitle:"API" -intitle:"Documentation" (site:.com OR site:.org) after:2023',

    # Música y audio profesional
    '(inurl:/shop OR inurl:/store OR inurl:/product OR inurl:/checkout OR inurl:/cart) (intext:"worldpay" OR intext:"worldpay.com" OR intext:"worldpay.js" OR intext:"worldpay payments") (intext:"music" OR "instruments" OR "guitar" OR "piano" OR "drums" OR "audio equipment" OR "studio" OR "recording" OR "microphone" OR "mixer" OR "amplifier" OR "professional audio" OR "DJ equipment" OR "sound system" OR "home theater") -site:worldpay.com -site:github.com -site:reddit.com -site:facebook.com -site:twitter.com -site:linkedin.com -site:instagram.com -inurl:/docs -inurl:/developer -inurl:/partners -inurl:/plugins -inurl:/integration -intext:"payment gateway" -intext:"reseller" -intext:"accept payments for clients" -intitle:"API" -intitle:"Documentation" (site:.com OR site:.org) after:2023',

    # Bebés y maternidad
    '(inurl:/shop OR inurl:/store OR inurl:/product OR inurl:/checkout OR inurl:/cart) (intext:"worldpay" OR intext:"worldpay.com" OR intext:"worldpay.js" OR intext:"worldpay payments") (intext:"baby" OR "kids" OR "children" OR "toys" OR "stroller" OR "diapers" OR "nursery" OR "maternity" OR "pregnancy" OR "infant" OR "toddler" OR "childcare" OR "parenting" OR "educational toys" OR "safety" OR "feeding") -site:worldpay.com -site:github.com -site:reddit.com -site:facebook.com -site:twitter.com -site:linkedin.com -site:instagram.com -inurl:/docs -inurl:/developer -inurl:/partners -inurl:/plugins -inurl:/integration -intext:"payment gateway" -intext:"reseller" -intext:"accept payments for clients" -intitle:"API" -intitle:"Documentation" (site:.com OR site:.org) after:2023',

    # Outdoor aventura
    '(inurl:/shop OR inurl:/store OR inurl:/product OR inurl:/checkout OR inurl:/cart) (intext:"worldpay" OR intext:"worldpay.com" OR intext:"worldpay.js" OR intext:"worldpay payments") (intext:"outdoor" OR "camping" OR "hiking" OR "fishing" OR "hunting" OR "survival gear" OR "backpacking" OR "mountaineering" OR "rock climbing" OR "kayaking" OR "canoeing" OR "adventure" OR "expedition" OR "wilderness" OR "nature") -site:worldpay.com -site:github.com -site:reddit.com -site:facebook.com -site:twitter.com -site:linkedin.com -site:instagram.com -inurl:/docs -inurl:/developer -inurl:/partners -inurl:/plugins -inurl:/integration -intext:"payment gateway" -intext:"reseller" -intext:"accept payments for clients" -intitle:"API" -intitle:"Documentation" (site:.com OR site:.org) after:2023',

    # Oficina y negocios
    '(inurl:/shop OR inurl:/store OR inurl:/product OR inurl:/checkout OR inurl:/cart) (intext:"worldpay" OR intext:"worldpay.com" OR intext:"worldpay.js" OR intext:"worldpay payments") (intext:"office supplies" OR "stationery" OR "printer" OR "desk" OR "chair" OR "notebook" OR "business" OR "corporate" OR "professional" OR "meeting" OR "presentation" OR "filing" OR "organization" OR "productivity") -site:worldpay.com -site:github.com -site:reddit.com -site:facebook.com -site:twitter.com -site:linkedin.com -site:instagram.com -inurl:/docs -inurl:/developer -inurl:/partners -inurl:/plugins -inurl:/integration -intext:"payment gateway" -intext:"reseller" -intext:"accept payments for clients" -intitle:"API" -intitle:"Documentation" (site:.com OR site:.org) after:2023',

    # Textiles y moda sostenible
    '(inurl:/shop OR inurl:/store OR inurl:/product OR inurl:/checkout OR inurl:/cart) (intext:"worldpay" OR intext:"worldpay.com" OR intext:"worldpay.js" OR intext:"worldpay payments") (intext:"sustainable" OR "eco-friendly" OR "organic cotton" OR "hemp" OR "bamboo" OR "recycled" OR "fair trade" OR "ethical fashion" OR "zero waste" OR "upcycled" OR "vintage" OR "secondhand" OR "thrift") -site:worldpay.com -site:github.com -site:reddit.com -site:facebook.com -site:twitter.com -site:linkedin.com -site:instagram.com -inurl:/docs -inurl:/developer -inurl:/partners -inurl:/plugins -inurl:/integration -intext:"payment gateway" -intext:"reseller" -intext:"accept payments for clients" -intitle:"API" -intitle:"Documentation" (site:.com OR site:.org) after:2023',

    # Servicios profesionales
    '(inurl:/shop OR inurl:/store OR inurl:/product OR inurl:/checkout OR inurl:/cart) (intext:"worldpay" OR intext:"worldpay.com" OR intext:"worldpay.js" OR intext:"worldpay payments") (intext:"consulting" OR "service" OR "professional" OR "coaching" OR "training" OR "workshop" OR "course" OR "certification" OR "therapy" OR "counseling" OR "legal" OR "accounting" OR "marketing") -site:worldpay.com -site:github.com -site:reddit.com -site:facebook.com -site:twitter.com -site:linkedin.com -site:instagram.com -inurl:/docs -inurl:/developer -inurl:/partners -inurl:/plugins -inurl:/integration -intext:"payment gateway" -intext:"reseller" -intext:"accept payments for clients" -intitle:"API" -intitle:"Documentation" (site:.com OR site:.org) after:2023',

    # Dorks específicos para Worldpay
    '(inurl:/shop OR inurl:/store OR inurl:/checkout) (intext:"Worldpay" OR intext:"worldpay.com" OR intext:"worldpay gateway") -site:worldpay.com -site:github.com',
    'intext:"worldpay.setPublishableKey" OR intext:"worldpay.createToken" (inurl:/payment OR inurl:/checkout) -site:worldpay.com -site:github.com',
    'intext:"worldpay.submit" OR intext:"wp_payment_form" (inurl:/shop OR inurl:/store) -site:worldpay.com -site:github.com',
    '(intext:"merchant code" OR intext:"installation id") AND intext:"worldpay" (inurl:/checkout OR inurl:/payment) -site:worldpay.com -site:github.com',
    'intext:"worldpay test" OR intext:"worldpay sandbox" (inurl:/test OR inurl:/demo OR inurl:/staging) -site:worldpay.com -site:github.com',
    'intext:"worldpay secure" OR intext:"worldpay encrypted" (inurl:/payment OR inurl:/secure) -site:worldpay.com -site:github.com',
    'intext:"worldpay hosted" OR intext:"worldpay iframe" (inurl:/checkout OR inurl:/payment) -site:worldpay.com -site:github.com',

    # Dorks genéricos adicionales para Worldpay
    '(inurl:/shop OR inurl:/store OR inurl:/product OR inurl:/checkout OR inurl:/cart) (intext:"worldpay" OR intext:"worldpay.com" OR intext:"worldpay.js" OR intext:"worldpay payments") -site:worldpay.com -site:github.com -site:reddit.com -site:facebook.com -site:twitter.com -site:linkedin.com -site:instagram.com -inurl:/docs -inurl:/developer -inurl:/partners -inurl:/plugins -inurl:/integration -intext:"payment gateway" -intext:"reseller" -intext:"accept payments for clients" -intitle:"API" -intitle:"Documentation" (site:.com OR site:.org) after:2023',

    # Dorks específicos para sitios .org con Worldpay
    'site:.org (inurl:/shop OR inurl:/store OR inurl:/checkout) (intext:"worldpay" OR intext:"worldpay.com") (intext:"nonprofit" OR "charity" OR "foundation") -site:worldpay.com -site:github.com',
    'site:.org (inurl:/donate OR inurl:/donation OR inurl:/give) (intext:"worldpay" OR intext:"worldpay.com") -site:worldpay.com -site:github.com',
    'site:.org (inurl:/merchandise OR inurl:/merch OR inurl:/gift) (intext:"worldpay" OR intext:"worldpay.com") -site:worldpay.com -site:github.com',
    'site:.org (intext:"museum store" OR "museum shop") (intext:"worldpay" OR intext:"worldpay.com") -site:worldpay.com -site:github.com',
    'site:.org (intext:"university store" OR "college store") (intext:"worldpay" OR intext:"worldpay.com") -site:worldpay.com -site:github.com',
    'site:.org (intext:"church store" OR "religious store") (intext:"worldpay" OR intext:"worldpay.com") -site:worldpay.com -site:github.com'
]

# Dorks de Square organizados por categorías
SQUARE_DORKS = [
    # Plantas y jardinería
    '(inurl:/shop OR inurl:/store OR inurl:/product OR inurl:/checkout OR inurl:/cart) (intext:"square" OR intext:"squareup" OR intext:"square.com" OR intext:"square checkout") (intext:"plant" OR "succulent" OR "cactus" OR "bonsai" OR "garden" OR "gardening" OR "nursery" OR "flower" OR "botanical" OR "houseplant" OR "terrarium" OR "fertilizer" OR "soil" OR "seeds") -site:squareup.com -site:github.com -site:reddit.com -site:facebook.com -site:twitter.com -site:linkedin.com -site:instagram.com -inurl:/docs -inurl:/developer -inurl:/partners -inurl:/plugins -inurl:/integration -intext:"payment gateway" -intext:"reseller" -intext:"accept payments for clients" -intitle:"API" -intitle:"Documentation" (site:.com OR site:.org) after:2023',

    # Ropa y moda
    '(inurl:/shop OR inurl:/store OR inurl:/product OR inurl:/checkout OR inurl:/cart) (intext:"square" OR intext:"squareup" OR intext:"square.com" OR intext:"square checkout") (intext:"clothing" OR "fashion" OR "apparel" OR "t-shirt" OR "shoes" OR "sneakers" OR "streetwear") -site:squareup.com -site:github.com -site:reddit.com -site:facebook.com -site:twitter.com -site:linkedin.com -site:instagram.com -inurl:/docs -inurl:/developer -inurl:/partners -inurl:/plugins -inurl:/integration -intext:"payment gateway" -intext:"reseller" -intext:"accept payments for clients" -intitle:"API" -intitle:"Documentation" (site:.com OR site:.org) after:2023',

    # Tecnología y gadgets
    '(inurl:/shop OR inurl:/store OR inurl:/product OR inurl:/checkout OR inurl:/cart) (intext:"square" OR intext:"squareup" OR intext:"square.com" OR intext:"square checkout") (intext:"electronics" OR "gadgets" OR "tech" OR "laptop" OR "phone" OR "charger" OR "smartwatch" OR "tablet" OR "device") -site:squareup.com -site:github.com -site:reddit.com -site:facebook.com -site:twitter.com -site:linkedin.com -site:instagram.com -inurl:/docs -inurl:/developer -inurl:/partners -inurl:/plugins -inurl:/integration -intext:"payment gateway" -intext:"reseller" -intext:"accept payments for clients" -intitle:"API" -intitle:"Documentation" (site:.com OR site:.org) after:2023',

    # Herramientas y construcción
    '(inurl:/shop OR inurl:/store OR inurl:/product OR inurl:/checkout OR inurl:/cart) (intext:"square" OR intext:"squareup" OR intext:"square.com" OR intext:"square checkout") (intext:"tools" OR "tool" OR "drill" OR "saw" OR "hammer" OR "construction" OR "hardware" OR "power tools" OR "screwdriver" OR "wrench") -site:squareup.com -site:github.com -site:reddit.com -site:facebook.com -site:twitter.com -site:linkedin.com -site:instagram.com -inurl:/docs -inurl:/developer -inurl:/partners -inurl:/plugins -inurl:/integration -intext:"payment gateway" -intext:"reseller" -intext:"accept payments for clients" -intitle:"API" -intitle:"Documentation" (site:.com OR site:.org) after:2023',

    # Libros y educación
    '(inurl:/shop OR inurl:/store OR inurl:/product OR inurl:/checkout OR inurl:/cart) (intext:"square" OR intext:"squareup" OR intext:"square.com" OR intext:"square checkout") (intext:"book" OR "books" OR "novel" OR "literature" OR "reading" OR "study" OR "learning" OR "course" OR "ebook") -site:squareup.com -site:github.com -site:reddit.com -site:facebook.com -site:twitter.com -site:linkedin.com -site:instagram.com -inurl:/docs -inurl:/developer -inurl:/partners -inurl:/plugins -inurl:/integration -intext:"payment gateway" -intext:"reseller" -intext:"accept payments for clients" -intitle:"API" -intitle:"Documentation" (site:.com OR site:.org) after:2023',

    # Mascotas
    '(inurl:/shop OR inurl:/store OR inurl:/product OR inurl:/checkout OR inurl:/cart) (intext:"square" OR intext:"squareup" OR intext:"square.com" OR intext:"square checkout") (intext:"pet" OR "pets" OR "dog" OR "cat" OR "leash" OR "pet toy" OR "collar" OR "treats" OR "pet food") -site:squareup.com -site:github.com -site:reddit.com -site:facebook.com -site:twitter.com -site:linkedin.com -site:instagram.com -inurl:/docs -inurl:/developer -inurl:/partners -inurl:/plugins -inurl:/integration -intext:"payment gateway" -intext:"reseller" -intext:"accept payments for clients" -intitle:"API" -intitle:"Documentation" (site:.com OR site:.org) after:2023',

    # Comida y bebida
    '(inurl:/shop OR inurl:/store OR inurl:/product OR inurl:/checkout OR inurl:/cart) (intext:"square" OR intext:"squareup" OR intext:"square.com" OR intext:"square checkout") (intext:"chocolate" OR "snack" OR "coffee" OR "tea" OR "organic" OR "vegan" OR "honey" OR "spice" OR "gourmet" OR "wine") -site:squareup.com -site:github.com -site:reddit.com -site:facebook.com -site:twitter.com -site:linkedin.com -site:instagram.com -inurl:/docs -inurl:/developer -inurl:/partners -inurl:/plugins -inurl:/integration -intext:"payment gateway" -intext:"reseller" -intext:"accept payments for clients" -intitle:"API" -intitle:"Documentation" (site:.com OR site:.org) after:2023',

    # Videojuegos y entretenimiento
    '(inurl:/shop OR inurl:/store OR inurl:/product OR inurl:/checkout OR inurl:/cart) (intext:"square" OR intext:"squareup" OR intext:"square.com" OR intext:"square checkout") (intext:"gaming" OR "games" OR "gamepad" OR "console" OR "PC game" OR "video game" OR "playstation" OR "xbox") -site:squareup.com -site:github.com -site:reddit.com -site:facebook.com -site:twitter.com -site:linkedin.com -site:instagram.com -inurl:/docs -inurl:/developer -inurl:/partners -inurl:/plugins -inurl:/integration -intext:"payment gateway" -intext:"reseller" -intext:"accept payments for clients" -intitle:"API" -intitle:"Documentation" (site:.com OR site:.org) after:2023',

    # Arte, diseño y decoración
    '(inurl:/shop OR inurl:/store OR inurl:/product OR inurl:/checkout OR inurl:/cart) (intext:"square" OR intext:"squareup" OR intext:"square.com" OR intext:"square checkout") (intext:"art" OR "prints" OR "canvas" OR "poster" OR "illustration" OR "decor" OR "home design" OR "interior") -site:squareup.com -site:github.com -site:reddit.com -site:facebook.com -site:twitter.com -site:linkedin.com -site:instagram.com -inurl:/docs -inurl:/developer -inurl:/partners -inurl:/plugins -inurl:/integration -intext:"payment gateway" -intext:"reseller" -intext:"accept payments for clients" -intitle:"API" -intitle:"Documentation" (site:.com OR site:.org) after:2023',

    # Joyas y accesorios
    '(inurl:/shop OR inurl:/store OR inurl:/product OR inurl:/checkout OR inurl:/cart) (intext:"square" OR intext:"squareup" OR intext:"square.com" OR intext:"square checkout") (intext:"jewelry" OR "jewellery" OR "necklace" OR "ring" OR "bracelet" OR "earrings" OR "watch" OR "accessories") -site:squareup.com -site:github.com -site:reddit.com -site:facebook.com -site:twitter.com -site:linkedin.com -site:instagram.com -inurl:/docs -inurl:/developer -inurl:/partners -inurl:/plugins -inurl:/integration -intext:"payment gateway" -intext:"reseller" -intext:"accept payments for clients" -intitle:"API" -intitle:"Documentation" (site:.com OR site:.org) after:2023',

    # Deportes y fitness
    '(inurl:/shop OR inurl:/store OR inurl:/product OR inurl:/checkout OR inurl:/cart) (intext:"square" OR intext:"squareup" OR intext:"square.com" OR intext:"square checkout") (intext:"sports" OR "fitness" OR "gym" OR "workout" OR "athletic" OR "running" OR "yoga" OR "exercise") -site:squareup.com -site:github.com -site:reddit.com -site:facebook.com -site:twitter.com -site:linkedin.com -site:instagram.com -inurl:/docs -inurl:/developer -inurl:/partners -inurl:/plugins -inurl:/integration -intext:"payment gateway" -intext:"reseller" -intext:"accept payments for clients" -intitle:"API" -intitle:"Documentation" (site:.com OR site:.org) after:2023',

    # Salud y belleza
    '(inurl:/shop OR inurl:/store OR inurl:/product OR inurl:/checkout OR inurl:/cart) (intext:"square" OR intext:"squareup" OR intext:"square.com" OR intext:"square checkout") (intext:"beauty" OR "cosmetics" OR "skincare" OR "makeup" OR "health" OR "supplements" OR "vitamins") -site:squareup.com -site:github.com -site:reddit.com -site:facebook.com -site:twitter.com -site:linkedin.com -site:instagram.com -inurl:/docs -inurl:/developer -inurl:/partners -inurl:/plugins -inurl:/integration -intext:"payment gateway" -intext:"reseller" -intext:"accept payments for clients" -intitle:"API" -intitle:"Documentation" (site:.com OR site:.org) after:2023',

    # Automotriz
    '(inurl:/shop OR inurl:/store OR inurl:/product OR inurl:/checkout OR inurl:/cart) (intext:"square" OR intext:"squareup" OR intext:"square.com" OR intext:"square checkout") (intext:"automotive" OR "car parts" OR "motorcycle" OR "auto accessories" OR "tires" OR "battery") -site:squareup.com -site:github.com -site:reddit.com -site:facebook.com -site:twitter.com -site:linkedin.com -site:instagram.com -inurl:/docs -inurl:/developer -inurl:/partners -inurl:/plugins -inurl:/integration -intext:"payment gateway" -intext:"reseller" -intext:"accept payments for clients" -intitle:"API" -intitle:"Documentation" (site:.com OR site:.org) after:2023',

    # Hogar y muebles
    '(inurl:/shop OR inurl:/store OR inurl:/product OR inurl:/checkout OR inurl:/cart) (intext:"square" OR intext:"squareup" OR intext:"square.com" OR intext:"square checkout") (intext:"furniture" OR "home goods" OR "kitchen" OR "appliances" OR "bedding" OR "lighting") -site:squareup.com -site:github.com -site:reddit.com -site:facebook.com -site:twitter.com -site:linkedin.com -site:instagram.com -inurl:/docs -inurl:/developer -inurl:/partners -inurl:/plugins -inurl:/integration -intext:"payment gateway" -intext:"reseller" -intext:"accept payments for clients" -intitle:"API" -intitle:"Documentation" (site:.com OR site:.org) after:2023',

    # Música y instrumentos
    '(inurl:/shop OR inurl:/store OR inurl:/product OR inurl:/checkout OR inurl:/cart) (intext:"square" OR intext:"squareup" OR intext:"square.com" OR intext:"square checkout") (intext:"music" OR "instruments" OR "guitar" OR "piano" OR "drums" OR "audio equipment") -site:squareup.com -site:github.com -site:reddit.com -site:facebook.com -site:twitter.com -site:linkedin.com -site:instagram.com -inurl:/docs -inurl:/developer -inurl:/partners -inurl:/plugins -inurl:/integration -intext:"payment gateway" -intext:"reseller" -intext:"accept payments for clients" -intitle:"API" -intitle:"Documentation" (site:.com OR site:.org) after:2023',

    # Bebés y niños
    '(inurl:/shop OR inurl:/store OR inurl:/product OR inurl:/checkout OR inurl:/cart) (intext:"square" OR intext:"squareup" OR intext:"square.com" OR intext:"square checkout") (intext:"baby" OR "kids" OR "children" OR "toys" OR "stroller" OR "diapers" OR "nursery") -site:squareup.com -site:github.com -site:reddit.com -site:facebook.com -site:twitter.com -site:linkedin.com -site:instagram.com -inurl:/docs -inurl:/developer -inurl:/partners -inurl:/plugins -inurl:/integration -intext:"payment gateway" -intext:"reseller" -intext:"accept payments for clients" -intitle:"API" -intitle:"Documentation" (site:.com OR site:.org) after:2023',

    # Outdoor y camping
    '(inurl:/shop OR inurl:/store OR inurl:/product OR inurl:/checkout OR inurl:/cart) (intext:"square" OR intext:"squareup" OR intext:"square.com" OR intext:"square checkout") (intext:"outdoor" OR "camping" OR "hiking" OR "fishing" OR "hunting" OR "survival gear") -site:squareup.com -site:github.com -site:reddit.com -site:facebook.com -site:twitter.com -site:linkedin.com -site:instagram.com -inurl:/docs -inurl:/developer -inurl:/partners -inurl:/plugins -inurl:/integration -intext:"payment gateway" -intext:"reseller" -intext:"accept payments for clients" -intitle:"API" -intitle:"Documentation" (site:.com OR site:.org) after:2023',

    # Oficina y papelería
    '(inurl:/shop OR inurl:/store OR inurl:/product OR inurl:/checkout OR inurl:/cart) (intext:"square" OR intext:"squareup" OR intext:"square.com" OR intext:"square checkout") (intext:"office supplies" OR "stationery" OR "printer" OR "desk" OR "chair" OR "notebook") -site:squareup.com -site:github.com -site:reddit.com -site:facebook.com -site:twitter.com -site:linkedin.com -site:instagram.com -inurl:/docs -inurl:/developer -inurl:/partners -inurl:/plugins -inurl:/integration -intext:"payment gateway" -intext:"reseller" -intext:"accept payments for clients" -intitle:"API" -intitle:"Documentation" (site:.com OR site:.org) after:2023',

    # Dorks específicos para Square
    'intext:"Square.ApplicationId" OR intext:"Square.setApplicationId" (inurl:/payment OR inurl:/checkout) -site:squareup.com -site:github.com',
    'intext:"square.com/v2/locations" OR intext:"sq0idp-" (inurl:/shop OR inurl:/store) -site:squareup.com -site:github.com',
    'intext:"SqPaymentForm" OR intext:"square-payment-form" (inurl:/checkout OR inurl:/payment) -site:squareup.com -site:github.com',
    'intext:"square sandbox" OR intext:"square test" (inurl:/test OR inurl:/demo OR inurl:/staging) -site:squareup.com -site:github.com'
]

# Dorks de Stripe organizados por categorías
STRIPE_DORKS = [
    # Plantas y jardinería
    '(inurl:/shop OR inurl:/store OR inurl:/product OR inurl:/checkout OR inurl:/cart) (intext:"pk_live_" OR intext:"Powered by Stripe" OR intext:"Pay with card") (intext:"plant" OR "succulent" OR "cactus" OR "bonsai" OR "garden" OR "gardening" OR "nursery" OR "flower" OR "botanical" OR "houseplant" OR "terrarium" OR "fertilizer" OR "soil" OR "seeds") -site:stripe.com -site:github.com -site:reddit.com -site:facebook.com -site:twitter.com -site:linkedin.com -site:instagram.com -inurl:/docs -inurl:/developer -inurl:/partners -inurl:/plugins -inurl:/integration -intext:"payment gateway" -intext:"reseller" -intext:"accept payments for clients" -intitle:"API" -intitle:"Documentation" (site:.com OR site:.org) after:2023',

    # Ropa y moda
    '(inurl:/shop OR inurl:/store OR inurl:/product OR inurl:/checkout OR inurl:/cart) (intext:"pk_live_" OR intext:"Powered by Stripe" OR intext:"Pay with card") (intext:"clothing" OR "fashion" OR "apparel" OR "t-shirt" OR "shoes" OR "sneakers" OR "streetwear" OR "dress" OR "jeans" OR "jacket" OR "coat" OR "hoodie" OR "pants" OR "shorts" OR "underwear" OR "socks" OR "hat" OR "cap" OR "scarf" OR "gloves") -site:stripe.com -site:github.com -site:reddit.com -site:facebook.com -site:twitter.com -site:linkedin.com -site:instagram.com -inurl:/docs -inurl:/developer -inurl:/partners -inurl:/plugins -inurl:/integration -intext:"payment gateway" -intext:"reseller" -intext:"accept payments for clients" -intitle:"API" -intitle:"Documentation" (site:.com OR site:.org) after:2023',

    # Tecnología y gadgets
    '(inurl:/shop OR inurl:/store OR inurl:/product OR inurl:/checkout OR inurl:/cart) (intext:"pk_live_" OR intext:"Powered by Stripe" OR intext:"Pay with card") (intext:"electronics" OR "gadgets" OR "tech" OR "laptop" OR "phone" OR "charger" OR "smartwatch" OR "tablet" OR "device" OR "computer" OR "mouse" OR "keyboard" OR "headphones" OR "speaker" OR "camera" OR "drone" OR "gaming" OR "console" OR "accessories") -site:stripe.com -site:github.com -site:reddit.com -site:facebook.com -site:twitter.com -site:linkedin.com -site:instagram.com -inurl:/docs -inurl:/developer -inurl:/partners -inurl:/plugins -inurl:/integration -intext:"payment gateway" -intext:"reseller" -intext:"accept payments for clients" -intitle:"API" -intitle:"Documentation" (site:.com OR site:.org) after:2023',

    # Herramientas y construcción
    '(inurl:/shop OR inurl:/store OR inurl:/product OR inurl:/checkout OR inurl:/cart) (intext:"pk_live_" OR intext:"Powered by Stripe" OR intext:"Pay with card") (intext:"tools" OR "tool" OR "drill" OR "saw" OR "hammer" OR "construction" OR "hardware" OR "power tools" OR "screwdriver" OR "wrench" OR "plumbing" OR "electrical" OR "ladder" OR "nails" OR "screws" OR "bolt" OR "nut" OR "paint" OR "brush" OR "measuring") -site:stripe.com -site:github.com -site:reddit.com -site:facebook.com -site:twitter.com -site:linkedin.com -site:instagram.com -inurl:/docs -inurl:/developer -inurl:/partners -inurl:/plugins -inurl:/integration -intext:"payment gateway" -intext:"reseller" -intext:"accept payments for clients" -intitle:"API" -intitle:"Documentation" (site:.com OR site:.org) after:2023',

    # Libros y educación
    '(inurl:/shop OR inurl:/store OR inurl:/product OR inurl:/checkout OR inurl:/cart) (intext:"pk_live_" OR intext:"Powered by Stripe" OR intext:"Pay with card") (intext:"book" OR "books" OR "novel" OR "literature" OR "reading" OR "study" OR "learning" OR "course" OR "ebook" OR "textbook" OR "magazine" OR "journal" OR "encyclopedia" OR "dictionary" OR "biography" OR "fiction" OR "non-fiction" OR "education" OR "academic") -site:stripe.com -site:github.com -site:reddit.com -site:facebook.com -site:twitter.com -site:linkedin.com -site:instagram.com -inurl:/docs -inurl:/developer -inurl:/partners -inurl:/plugins -inurl:/integration -intext:"payment gateway" -intext:"reseller" -intext:"accept payments for clients" -intitle:"API" -intitle:"Documentation" (site:.com OR site:.org) after:2023',

    # Mascotas
    '(inurl:/shop OR inurl:/store OR inurl:/product OR inurl:/checkout OR inurl:/cart) (intext:"pk_live_" OR intext:"Powered by Stripe" OR intext:"Pay with card") (intext:"pet" OR "pets" OR "dog" OR "cat" OR "leash" OR "pet toy" OR "collar" OR "treats" OR "pet food" OR "aquarium" OR "bird" OR "reptile" OR "hamster" OR "rabbit" OR "fish" OR "grooming" OR "vet" OR "carrier" OR "bed" OR "house") -site:stripe.com -site:github.com -site:reddit.com -site:facebook.com -site:twitter.com -site:linkedin.com -site:instagram.com -inurl:/docs -inurl:/developer -inurl:/partners -inurl:/plugins -inurl:/integration -intext:"payment gateway" -intext:"reseller" -intext:"accept payments for clients" -intitle:"API" -intitle:"Documentation" (site:.com OR site:.org) after:2023',

    # Comida y bebida
    '(inurl:/shop OR inurl:/store OR inurl:/product OR inurl:/checkout OR inurl:/cart) (intext:"pk_live_" OR intext:"Powered by Stripe" OR intext:"Pay with card") (intext:"chocolate" OR "snack" OR "coffee" OR "tea" OR "organic" OR "vegan" OR "honey" OR "spice" OR "gourmet" OR "wine" OR "beer" OR "whiskey" OR "vodka" OR "rum" OR "juice" OR "soda" OR "water" OR "energy drink" OR "supplement" OR "protein") -site:stripe.com -site:github.com -site:reddit.com -site:facebook.com -site:twitter.com -site:linkedin.com -site:instagram.com -inurl:/docs -inurl:/developer -inurl:/partners -inurl:/plugins -inurl:/integration -intext:"payment gateway" -intext:"reseller" -intext:"accept payments for clients" -intitle:"API" -intitle:"Documentation" (site:.com OR site:.org) after:2023',

    # Videojuegos y entretenimiento
    '(inurl:/shop OR inurl:/store OR inurl:/product OR inurl:/checkout OR inurl:/cart) (intext:"pk_live_" OR intext:"Powered by Stripe" OR intext:"Pay with card") (intext:"gaming" OR "games" OR "gamepad" OR "console" OR "PC game" OR "video game" OR "playstation" OR "xbox" OR "nintendo" OR "steam" OR "board game" OR "card game" OR "puzzle" OR "toy" OR "collectible" OR "figure" OR "model") -site:stripe.com -site:github.com -site:reddit.com -site:facebook.com -site:twitter.com -site:linkedin.com -site:instagram.com -inurl:/docs -inurl:/developer -inurl:/partners -inurl:/plugins -inurl:/integration -intext:"payment gateway" -intext:"reseller" -intext:"accept payments for clients" -intitle:"API" -intitle:"Documentation" (site:.com OR site:.org) after:2023',

    # Arte, diseño y decoración
    '(inurl:/shop OR inurl:/store OR inurl:/product OR inurl:/checkout OR inurl:/cart) (intext:"pk_live_" OR intext:"Powered by Stripe" OR intext:"Pay with card") (intext:"art" OR "prints" OR "canvas" OR "poster" OR "illustration" OR "decor" OR "home design" OR "interior" OR "painting" OR "sculpture" OR "photography" OR "frame" OR "wall art" OR "handmade" OR "craft" OR "ceramic" OR "pottery" OR "vintage" OR "antique") -site:stripe.com -site:github.com -site:reddit.com -site:facebook.com -site:twitter.com -site:linkedin.com -site:instagram.com -inurl:/docs -inurl:/developer -inurl:/partners -inurl:/plugins -inurl:/integration -intext:"payment gateway" -intext:"reseller" -intext:"accept payments for clients" -intitle:"API" -intitle:"Documentation" (site:.com OR site:.org) after:2023',

    # Joyas y accesorios
    '(inurl:/shop OR inurl:/store OR inurl:/product OR inurl:/checkout OR inurl:/cart) (intext:"pk_live_" OR intext:"Powered by Stripe" OR intext:"Pay with card") (intext:"jewelry" OR "jewellery" OR "necklace" OR "ring" OR "bracelet" OR "earrings" OR "watch" OR "accessories" OR "diamond" OR "gold" OR "silver" OR "platinum" OR "pearl" OR "gemstone" OR "charm" OR "pendant" OR "chain" OR "cufflinks" OR "brooch") -site:stripe.com -site:github.com -site:reddit.com -site:facebook.com -site:twitter.com -site:linkedin.com -site:instagram.com -inurl:/docs -inurl:/developer -inurl:/partners -inurl:/plugins -inurl:/integration -intext:"payment gateway" -intext:"reseller" -intext:"accept payments for clients" -intitle:"API" -intitle:"Documentation" (site:.com OR site:.org) after:2023',

    # Deportes y fitness
    '(inurl:/shop OR inurl:/store OR inurl:/product OR inurl:/checkout OR inurl:/cart) (intext:"pk_live_" OR intext:"Powered by Stripe" OR intext:"Pay with card") (intext:"sports" OR "fitness" OR "gym" OR "workout" OR "athletic" OR "running" OR "yoga" OR "exercise" OR "weights" OR "dumbbells" OR "treadmill" OR "bike" OR "bicycle" OR "skateboard" OR "surfboard" OR "skiing" OR "snowboard" OR "tennis" OR "golf" OR "basketball" OR "football" OR "soccer") -site:stripe.com -site:github.com -site:reddit.com -site:facebook.com -site:twitter.com -site:linkedin.com -site:instagram.com -inurl:/docs -inurl:/developer -inurl:/partners -inurl:/plugins -inurl:/integration -intext:"payment gateway" -intext:"reseller" -intext:"accept payments for clients" -intitle:"API" -intitle:"Documentation" (site:.com OR site:.org) after:2023',

    # Salud y belleza
    '(inurl:/shop OR inurl:/store OR inurl:/product OR inurl:/checkout OR inurl:/cart) (intext:"pk_live_" OR intext:"Powered by Stripe" OR intext:"Pay with card") (intext:"beauty" OR "cosmetics" OR "skincare" OR "makeup" OR "health" OR "supplements" OR "vitamins" OR "perfume" OR "cologne" OR "nail" OR "hair" OR "shampoo" OR "conditioner" OR "lotion" OR "cream" OR "serum" OR "mask" OR "spa" OR "wellness") -site:stripe.com -site:github.com -site:reddit.com -site:facebook.com -site:twitter.com -site:linkedin.com -site:instagram.com -inurl:/docs -inurl:/developer -inurl:/partners -inurl:/plugins -inurl:/integration -intext:"payment gateway" -intext:"reseller" -intext:"accept payments for clients" -intitle:"API" -intitle:"Documentation" (site:.com OR site:.org) after:2023',

    # Automotriz
    '(inurl:/shop OR inurl:/store OR inurl:/product OR inurl:/checkout OR inurl:/cart) (intext:"pk_live_" OR intext:"Powered by Stripe" OR intext:"Pay with card") (intext:"automotive" OR "car parts" OR "motorcycle" OR "auto accessories" OR "tires" OR "battery" OR "engine" OR "brake" OR "oil" OR "filter" OR "spark plug" OR "transmission" OR "exhaust" OR "suspension" OR "headlight" OR "taillight" OR "mirror" OR "steering" OR "seat cover") -site:stripe.com -site:github.com -site:reddit.com -site:facebook.com -site:twitter.com -site:linkedin.com -site:instagram.com -inurl:/docs -inurl:/developer -inurl:/partners -inurl:/plugins -inurl:/integration -intext:"payment gateway" -intext:"reseller" -intext:"accept payments for clients" -intitle:"API" -intitle:"Documentation" (site:.com OR site:.org) after:2023',

    # Hogar y muebles
    '(inurl:/shop OR inurl:/store OR inurl:/product OR inurl:/checkout OR inurl:/cart) (intext:"pk_live_" OR intext:"Powered by Stripe" OR intext:"Pay with card") (intext:"furniture" OR "home goods" OR "kitchen" OR "appliances" OR "bedding" OR "lighting" OR "sofa" OR "chair" OR "table" OR "bed" OR "mattress" OR "pillow" OR "blanket" OR "curtain" OR "rug" OR "carpet" OR "lamp" OR "mirror" OR "storage" OR "organization") -site:stripe.com -site:github.com -site:reddit.com -site:facebook.com -site:twitter.com -site:linkedin.com -site:instagram.com -inurl:/docs -inurl:/developer -inurl:/partners -inurl:/plugins -inurl:/integration -intext:"payment gateway" -intext:"reseller" -intext:"accept payments for clients" -intitle:"API" -intitle:"Documentation" (site:.com OR site:.org) after:2023',

    # Música y instrumentos
    '(inurl:/shop OR inurl:/store OR inurl:/product OR inurl:/checkout OR inurl:/cart) (intext:"pk_live_" OR intext:"Powered by Stripe" OR intext:"Pay with card") (intext:"music" OR "instruments" OR "guitar" OR "piano" OR "drums" OR "audio equipment" OR "violin" OR "trumpet" OR "saxophone" OR "flute" OR "bass" OR "microphone" OR "speaker" OR "amplifier" OR "synthesizer" OR "DJ" OR "turntable" OR "vinyl" OR "record" OR "CD") -site:stripe.com -site:github.com -site:reddit.com -site:facebook.com -site:twitter.com -site:linkedin.com -site:instagram.com -inurl:/docs -inurl:/developer -inurl:/partners -inurl:/plugins -inurl:/integration -intext:"payment gateway" -intext:"reseller" -intext:"accept payments for clients" -intitle:"API" -intitle:"Documentation" (site:.com OR site:.org) after:2023',

    # Bebés y niños
    '(inurl:/shop OR inurl:/store OR inurl:/product OR inurl:/checkout OR inurl:/cart) (intext:"pk_live_" OR intext:"Powered by Stripe" OR intext:"Pay with card") (intext:"baby" OR "kids" OR "children" OR "toys" OR "stroller" OR "diapers" OR "nursery" OR "crib" OR "car seat" OR "high chair" OR "playpen" OR "bottle" OR "pacifier" OR "clothing" OR "shoes" OR "educational" OR "learning" OR "infant" OR "toddler") -site:stripe.com -site:github.com -site:reddit.com -site:facebook.com -site:twitter.com -site:linkedin.com -site:instagram.com -inurl:/docs -inurl:/developer -inurl:/partners -inurl:/plugins -inurl:/integration -intext:"payment gateway" -intext:"reseller" -intext:"accept payments for clients" -intitle:"API" -intitle:"Documentation" (site:.com OR site:.org) after:2023',

    # Outdoor y camping
    '(inurl:/shop OR inurl:/store OR inurl:/product OR inurl:/checkout OR inurl:/cart) (intext:"pk_live_" OR intext:"Powered by Stripe" OR intext:"Pay with card") (intext:"outdoor" OR "camping" OR "hiking" OR "fishing" OR "hunting" OR "survival gear" OR "tent" OR "sleeping bag" OR "backpack" OR "boots" OR "jacket" OR "compass" OR "knife" OR "flashlight" OR "rope" OR "climbing" OR "kayak" OR "canoe" OR "binoculars") -site:stripe.com -site:github.com -site:reddit.com -site:facebook.com -site:twitter.com -site:linkedin.com -site:instagram.com -inurl:/docs -inurl:/developer -inurl:/partners -inurl:/plugins -inurl:/integration -intext:"payment gateway" -intext:"reseller" -intext:"accept payments for clients" -intitle:"API" -intitle:"Documentation" (site:.com OR site:.org) after:2023',

    # Oficina y papelería
    '(inurl:/shop OR inurl:/store OR inurl:/product OR inurl:/checkout OR inurl:/cart) (intext:"pk_live_" OR intext:"Powered by Stripe" OR intext:"Pay with card") (intext:"office supplies" OR "stationery" OR "printer" OR "desk" OR "chair" OR "notebook" OR "pen" OR "pencil" OR "paper" OR "folder" OR "binder" OR "calculator" OR "stapler" OR "tape" OR "scissors" OR "organizer" OR "filing" OR "envelope" OR "label") -site:stripe.com -site:github.com -site:reddit.com -site:facebook.com -site:twitter.com -site:linkedin.com -site:instagram.com -inurl:/docs -inurl:/developer -inurl:/partners -inurl:/plugins -inurl:/integration -intext:"payment gateway" -intext:"reseller" -intext:"accept payments for clients" -intitle:"API" -intitle:"Documentation" (site:.com OR site:.org) after:2023',

    # Médico y farmacia
    '(inurl:/shop OR inurl:/store OR inurl:/product OR inurl:/checkout OR inurl:/cart) (intext:"pk_live_" OR intext:"Powered by Stripe" OR intext:"Pay with card") (intext:"medical" OR "pharmacy" OR "medicine" OR "prescription" OR "health care" OR "first aid" OR "bandage" OR "thermometer" OR "stethoscope" OR "blood pressure" OR "glucose" OR "dental" OR "surgical" OR "hospital" OR "clinic" OR "equipment") -site:stripe.com -site:github.com -site:reddit.com -site:facebook.com -site:twitter.com -site:linkedin.com -site:instagram.com -inurl:/docs -inurl:/developer -inurl:/partners -inurl:/plugins -inurl:/integration -intext:"payment gateway" -intext:"reseller" -intext:"accept payments for clients" -intitle:"API" -intitle:"Documentation" (site:.com OR site:.org) after:2023',

    # Servicios profesionales
    '(inurl:/shop OR inurl:/store OR inurl:/product OR inurl:/checkout OR inurl:/cart) (intext:"pk_live_" OR intext:"Powered by Stripe" OR intext:"Pay with card") (intext:"consulting" OR "service" OR "professional" OR "legal" OR "accounting" OR "marketing" OR "design" OR "photography" OR "wedding" OR "event" OR "cleaning" OR "maintenance" OR "repair" OR "installation" OR "coaching" OR "training") -site:stripe.com -site:github.com -site:reddit.com -site:facebook.com -site:twitter.com -site:linkedin.com -site:instagram.com -inurl:/docs -inurl:/developer -inurl:/partners -inurl:/plugins -inurl:/integration -intext:"payment gateway" -intext:"reseller" -intext:"accept payments for clients" -intitle:"API" -intitle:"Documentation" (site:.com OR site:.org) after:2023',

    # Textiles y manualidades
    '(inurl:/shop OR inurl:/store OR inurl:/product OR inurl:/checkout OR inurl:/cart) (intext:"pk_live_" OR intext:"Powered by Stripe" OR intext:"Pay with card") (intext:"fabric" OR "textile" OR "sewing" OR "knitting" OR "crochet" OR "embroidery" OR "quilting" OR "yarn" OR "thread" OR "needle" OR "pattern" OR "craft" OR "DIY" OR "scrapbook" OR "beads" OR "ribbon" OR "button") -site:stripe.com -site:github.com -site:reddit.com -site:facebook.com -site:twitter.com -site:linkedin.com -site:instagram.com -inurl:/docs -inurl:/developer -inurl:/partners -inurl:/plugins -inurl:/integration -intext:"payment gateway" -intext:"reseller" -intext:"accept payments for clients" -intitle:"API" -intitle:"Documentation" (site:.com OR site:.org) after:2023',

    # Dorks genéricos adicionales
    '(inurl:/shop OR inurl:/store OR inurl:/product OR inurl:/checkout OR inurl:/cart) (intext:"pk_live_" OR intext:"Powered by Stripe" OR intext:"Pay with card") -site:stripe.com -site:github.com -site:reddit.com -site:facebook.com -site:twitter.com -site:linkedin.com -site:instagram.com -inurl:/docs -inurl:/developer -inurl:/partners -inurl:/plugins -inurl:/integration -intext:"payment gateway" -intext:"reseller" -intext:"accept payments for clients" -intitle:"API" -intitle:"Documentation" (site:.com OR site:.org) after:2023',

    # Dorks específicos para sitios .org - Organizaciones y tiendas
    'site:.org (inurl:/shop OR inurl:/store OR inurl:/checkout) (intext:"pk_live_" OR intext:"Powered by Stripe") (intext:"nonprofit" OR "charity" OR "foundation") -site:stripe.com -site:github.com',
    'site:.org (inurl:/donate OR inurl:/donation OR inurl:/give) (intext:"pk_live_" OR intext:"Powered by Stripe") -site:stripe.com -site:github.com',
    'site:.org (inurl:/merchandise OR inurl:/merch OR inurl:/gift) (intext:"pk_live_" OR intext:"Powered by Stripe") -site:stripe.com -site:github.com',
    'site:.org (intext:"museum store" OR "museum shop") (intext:"pk_live_" OR intext:"Powered by Stripe") -site:stripe.com -site:github.com',
    'site:.org (intext:"university store" OR "college store") (intext:"pk_live_" OR intext:"Powered by Stripe") -site:stripe.com -site:github.com',
    'site:.org (intext:"church store" OR "religious store") (intext:"pk_live_" OR intext:"Powered by Stripe") -site:stripe.com -site:github.com',
    'site:.org (intext:"wildlife" OR "conservation" OR "environment") (inurl:/shop OR inurl:/store) (intext:"pk_live_" OR intext:"Powered by Stripe") -site:stripe.com',
    'site:.org (intext:"art gallery" OR "artist" OR "craft") (inurl:/shop OR inurl:/store) (intext:"pk_live_" OR intext:"Powered by Stripe") -site:stripe.com',
    'site:.org (intext:"community" OR "local" OR "neighborhood") (inurl:/shop OR inurl:/store) (intext:"pk_live_" OR intext:"Powered by Stripe") -site:stripe.com',
    'site:.org (intext:"health" OR "medical" OR "wellness") (inurl:/shop OR inurl:/store) (intext:"pk_live_" OR intext:"Powered by Stripe") -site:stripe.com',
    'site:.org (intext:"education" OR "school" OR "learning") (inurl:/shop OR inurl:/store) (intext:"pk_live_" OR intext:"Powered by Stripe") -site:stripe.com',
    'site:.org (intext:"sports club" OR "athletic" OR "team") (inurl:/shop OR inurl:/store) (intext:"pk_live_" OR intext:"Powered by Stripe") -site:stripe.com',
    'site:.org (intext:"library" OR "book" OR "reading") (inurl:/shop OR inurl:/store) (intext:"pk_live_" OR intext:"Powered by Stripe") -site:stripe.com',
    'site:.org (intext:"festival" OR "event" OR "conference") (inurl:/shop OR inurl:/store OR inurl:/ticket) (intext:"pk_live_" OR intext:"Powered by Stripe") -site:stripe.com',
    'site:.org (intext:"volunteer" OR "service" OR "humanitarian") (inurl:/shop OR inurl:/store) (intext:"pk_live_" OR intext:"Powered by Stripe") -site:stripe.com'
]
