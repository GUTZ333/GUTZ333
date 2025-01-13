import mysql.connector

class SqlSERVER():
    def __init__(self):
        self.connect = mysql.connector.connect(
            host="localhost",
            user="root",
            password="hYZr8.Q-.pC9Nv2",
            database="GUTZ333"
        )
        self.query = self.connect.cursor()
    def dataAccountAttributes(self, name=None, email=None, password=None, phone=None):
        self.name_value = name
        self.email_value = email
        self.password_value = password
        self.phone_value = phone

    def productAttributes(self, name_product=None,image_product=None, price_product=None, unity_product=None, description_product=None, date_product=None):
        self.name_product = name_product
        self.image_product = image_product
        self.price_product = price_product
        self.unity_product = unity_product
        self.description_product = description_product
        self.date_product = date_product

    def SignIn(self, flash, redirect, url_for, render_template):
        self.query.execute(f"""
        SELECT * FROM register_users
        WHERE emailUser = '{self.email_value}' AND passwordUser = UNHEX(SHA2('{self.password_value}', 256));)
        """)
        search_account = self.query.fetchall()
        if search_account:
            flash("* authentication error", "authenticationError")
            return redirect(url_for("signIn"))
        else:
            return "<h1> login realizado com sucesso </h1>"
    def SignUp(self, flash, redirect, url_for, render_templates):
        self.query.execute(f"""
        SELECT 'Name exist' AS consult_accounts
        FROM register_users
        WHERE nameUser = '{self.name_value}'
        UNION ALL
        SELECT 'Email exist' AS consult_accounts
        FROM register_users
        WHERE emailUser = '{self.email_value}'
        UNION ALL
        SELECT 'Password exist' AS consult_accounts
        FROM register_users
        WHERE passwordUser = UNHEX(SHA2('{self.password_value}', 256))
        UNION ALL
        SELECT 'Phone exist' AS consult_accounts
        FROM register_users
        WHERE phoneUser = '{self.phone_value}';
        """)
        search_account = self.query.fetchall()
        if search_account:
            for lines in search_account:
                if "Name exist" in lines:
                    flash("* this name already exist.", "nameInput")
                if "Email exist" in lines:
                    flash("* this email already exist.", "emailInput")
                if "Password exist" in lines:
                    flash("* this password already exist.", "passwordInput")
                if "Phone exist" in lines:
                    flash("* this phone already exist.", "phoneInput")
            return redirect(url_for("signUp"))
        else:
            self.query.execute(f"""
                INSERT INTO register_users (nameUser, emailUser, passwordUser, phoneUser)
                VALUES ('{self.name_value}', '{self.email_value}', UNHEX(SHA2('{self.password_value}', 256)), '{self.phone_value}');
            """)
            self.connect.commit()
            self.connect.close()
            return "<h1> Conta Criada Com sucesso </h1>"
        
    def insertProducts(self):
        pass
    def SearchProducts(self):
        self.query.execute(f"""
        SELECT * FROM products
        where name_product = '{self.name_product}'
        """)
        search_product = self.query.fetchall()
        if search_product:
            pass
        else:
            pass