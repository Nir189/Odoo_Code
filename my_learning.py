# Odoo_Code


class MyController(http.Controller):
    @http.route('/website_form/',type='http', auth="public", methods=['POST','GET'], website=True , csrf=False)
    	# Here the code for contact form
    	# You can also hit this url from postman to check the response
    	# url="https://localhost:8069/create_lead"
        url="https://stage.o2btechnologies.com/create_lead"
        headers = {'content-type': 'application/json'}
        login = False
        password = False
        db = False

        if not request.env.user.has_group("base.group_public"):
            login=request.env.user.login
            print("i am insied if................", request.env)
            print("i am insied if................", request.env.user)
            password='1234'
            # password=request.env.user.password
            db = request._cr.dbname
        print("login passs db...............................",login,password,db)
        params = {
            "params":{
                "login":login,
                "password":password,
                "db":db,
                "name":name, 
                "email_from":email_from,
                "contact_name":name,
                "phone":number,
                "Question":subject,
                "description":description,
                "partner_name":company,
                "subject":subject,
                "page_url": page_url
                }
            }

        payload=json.dumps(params)
        #response = requests.post(url, params=params, headers=headers)
        response = requests.request("POST", url, data=payload, headers=headers)
        print("Checking the value.........................",response.text)


# It is an example for creating an api and sending response
class CrmLead(http.Controller):
    @http.route(['/create_lead'], type='json', auth='none', methods=['POST'], website=True, csrf=False)
    def create_lead(self, **kw):
        login = False
        password = False
        db = False
        login = kw.get('login')
        db = kw.get('db')
        password = kw.get('password')
        
        if not login or not password or not db:
            return {'message': 'authentication required.'}

        name = ''
        email_from=''
        contact_name=''
        phone = ''
        Question=''
        page_url=''
        subject=''
        description = ''
        partner_name =''


        if 'name' in kw and kw.get('name'):
            name= kw.get('name')
        if 'email_from' in kw and kw.get('email_from'):
            email_from= kw.get('email_from')
        if 'phone' in kw and kw.get('phone'):
            phone= kw.get('phone')
        if 'Question' in kw and kw.get('Question'):
            Question= kw.get('Question')
        if 'page_url' in kw and kw.get('page_url'):
            page_url= kw.get('page_url')
        if 'subject' in kw and kw.get('subject'):
            subject= kw.get('subject')
        if 'description' in kw and kw.get('description'):
            description= kw.get('description')
        if 'partner_name' in kw and kw.get('partner_name'):
            partner_name= kw.get('partner_name')
        if 'contact_name' in kw and kw.get('contact_name'):
            contact_name= kw.get('contact_name')

        vals = {
            'name':name,
            'email_from':email_from,
            'contact_name':contact_name,
            'phone':phone,
            'Question':Question,
            'description':description,
            'partner_name':partner_name,
            'subject':subject,
            'page_url': page_url
         }

        new_lead = request.env['crm.lead'].sudo().create(vals)
        args = {'success': True, 'message': 'Success', 'ID':new_lead.id}
    
        return args



    @http.route(['/material_list'], type='json', auth="none", methods=['POST'], website=True)
    def material_list_for_mrp(self, **kw):
        print("Checking c......................",kw)
        # authentication check
        login = False
        password = False
        db = False
        login = kw.get('login')
        db = kw.get('db')
        password = kw.get('password')
        if not login or not password or not db:
            return {'message': 'authentication required.'}