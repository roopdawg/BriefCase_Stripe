import streamlit as st
from streamlit.components.v1 import html
import streamlit.components.v1 as components
import os


# Get the Stripe publishable key from the environment variable
stripe_publishable_key = os.environ.get("STRIPE_KEY")

terms_and_conditions = '''
BriefCase Terms and Conditions

1. Acceptance of Terms

By accessing or using the BriefCase app ("BriefCase"), you agree to be bound by these Terms and Conditions. If you do not agree to these terms, you may not access or use BriefCase.

2. Use of BriefCase

You may use BriefCase only for lawful purposes and in accordance with these Terms and Conditions.
You agree not to use BriefCase:
In any way that violates any applicable federal, state, local, or international law or regulation.
To upload, transmit, or otherwise make available any material that is unlawful, harmful, threatening, abusive, harassing, tortious, defamatory, vulgar, obscene, libelous, invasive of another's privacy, hateful, or racially, ethnically, or otherwise objectionable.   
To impersonate any person or entity, or falsely state or otherwise misrepresent your affiliation with a person or entity.
To interfere with or disrupt the operation of BriefCase or the servers or networks connected to BriefCase, or disobey any requirements, procedures, policies, or regulations of networks connected to BriefCase.   
3. User Content

You are solely responsible for any content that you upload, transmit, or otherwise make available through BriefCase ("User Content").
You represent and warrant that:
You own or have the necessary licenses, rights, consents, and permissions to use and authorize us to use all User Content that you submit to BriefCase.   
All User Content is publicly available material and does not contain any confidential or proprietary information.
4. Disclaimer of Warranties

BriefCase is provided on an "as is" and "as available" basis.
We make no representations or warranties of any kind, express or implied, as to the operation of BriefCase or the information, content, materials, or products included on BriefCase.   
You expressly agree that your use of BriefCase is at your sole risk.
5. Limitation of Liability

We shall not be liable for any damages of any kind arising from the use of BriefCase, including, but not limited to, direct, indirect, incidental, punitive, and consequential damages.
 6. Indemnification

You agree to indemnify, defend, and hold harmless us, our affiliates, officers, directors, employees, agents, and licensors from and against any and all claims, liabilities, damages, losses, costs, expenses, or fees (including reasonable attorneys' fees) arising from your use of BriefCase or your violation of these Terms and Conditions.   
7. Billing

We use Stripe to process payments for BriefCase.
By using BriefCase, you agree to be bound by Stripe's terms of service.
You agree to pay all fees and charges incurred in connection with your use of BriefCase, including any applicable taxes.
8. Confidentiality

We will treat any personally identifiable information that you provide through BriefCase in accordance with our Privacy Policy.
You agree not to disclose any confidential information obtained through BriefCase to any third party without our prior written consent.
9. Modifications to BriefCase

We reserve the right to modify or discontinue, temporarily or permanently, BriefCase or any part thereof with or without notice.
You agree that we shall not be liable to you or to any third party for any modification, suspension, or discontinuance of BriefCase.   
10. Governing Law

These Terms and Conditions shall be governed by and construed in accordance with the laws of the State of California, without giving effect to any principles of conflicts of law.   
 11. Dispute Resolution

Any dispute arising out of or relating to these Terms and Conditions or BriefCase shall be resolved through binding arbitration in accordance with the rules of the American Arbitration Association.   
12. Entire Agreement

These Terms and Conditions constitute the entire agreement between you and us regarding the use of BriefCase and supersede all prior or contemporaneous communications and proposals, whether oral or written, between you and us.

If you have any questions or concerns regarding these terms, please contact us before confirming your subscription at support@luri.ai.
'''

#stripe_checkout_url_monthly = "https://buy.stripe.com/cN28xvbxj1lRd6U8wx"
#stripe_checkout_url_annual = "https://buy.stripe.com/8wM2971WJe8Dff2288"

terms_state = False

# Set page configuration
st.set_page_config(
    page_title="Subscribe to Briefcase using Stripe",
    layout="wide",
    initial_sidebar_state="expanded",
)

# Sidebar navigation
st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ("Monthly Subscription", "Annual Subscription", "Terms & Conditions"))

# First Subscription option 
if page == "Monthly Subscription":
    st.title("Renew your BriefCase subscription on a monthly basis")
    st.expander("View & Confirm Agreement")
    if st.checkbox("I agree to the Terms and Conditions", value=terms_state):
            terms_state = True

     # Show the modal with the legal terms when the terms button is clicked
    if terms_state:
       confirm_button = st.button("Confirm & Pay", disabled=not terms_state)
        # Show the modal with the legal terms when the terms button is clicked
       if confirm_button:
            terms_state = False
            conn.commit()
            conn.close()
            stripe_js = """
            <script async src="https://js.stripe.com/v3/buy-button.js"></script>
            <stripe-buy-button
            buy-button-id="buy_btn_1Pmld7BqWfU9o3QlYb7IJn04"	
            publishable-key="pk_live_51PmkRJBqWfU9o3Ql8aJH7gsPYqjWE7BvMU2pQpjyrfcsGEyFFbpDZt7yBiKbPwDYc4x2e2Tyx7KulO4VjsfoKDM400QrGD3Ylj"
            ></stripe-buy-button>
            """.format(stripe_publishable_key)
            # user next steps for payment
            st.write("Thanks for confirming the terms and conditions!")
            st.write("""""")
            st.title("Payment")
            html(stripe_js)
        

# Second subscription option 
elif page == "Annual Subscription":
    st.title("Renew your BriefCase subscription annually")
    st.expander("View & Confirm Agreement")
    if st.checkbox("I agree to the Terms and Conditions", value=terms_state):
            terms_state = True

     # Show the modal with the legal terms when the terms button is clicked
    if terms_state:
       confirm_button = st.button("Confirm & Pay", disabled=not terms_state)
        # Show the modal with the legal terms when the terms button is clicked
       if confirm_button:
            terms_state = False
            conn.commit()
            conn.close()
            stripe_js = """
            <script async src="https://js.stripe.com/v3/buy-button.js"></script>
            <stripe-buy-button
            buy-button-id="buy_btn_1PmkwhBqWfU9o3QlQwEd8Nso"
            publishable-key="pk_live_51PmkRJBqWfU9o3Ql8aJH7gsPYqjWE7BvMU2pQpjyrfcsGEyFFbpDZt7yBiKbPwDYc4x2e2Tyx7KulO4VjsfoKDM400QrGD3Ylj"
            ></stripe-buy-button>
            """.format(stripe_publishable_key)
            # user next steps for payment
            st.write("Thanks for confirming the terms and conditions!")
            st.write("""""")
            st.title("Payment")
            html(stripe_js)
            #st.image("beach_payment.png", caption="Scan the QR code to pay")
            #url = "https://mainnet.demo.btcpayserver.org/api/v1/invoices?storeId=4r8DKKKMkxGPVKcW9TXB2eta7PTVzzs192TWM3KuY52e&price=100&currency=USD&defaultPaymentMethod=BTC"
            #link='Pay wit BTC [via this link](https://mainnet.demo.btcpayserver.org/api/v1/invoices?storeId=4r8DKKKMkxGPVKcW9TXB2eta7PTVzzs192TWM3KuY52e&price=100&currency=USD&defaultPaymentMethod=BTC)'
            #st.markdown(link,unsafe_allow_html=True)
            #components.iframe(url,width = 300,height = 500, scrolling=True)
   
# Terms & Conditions page
if page == "Terms & Conditions":
        st.info(terms_and_conditions)
