import streamlit as st
from streamlit.components.v1 import html
import streamlit.components.v1 as components
import os


# Get the Stripe publishable key from the environment variable
stripe_publishable_key = os.environ.get("STRIPE_KEY")

terms_and_conditions = '''
BriefCase Terms and Conditions
Acceptance of Terms
By accessing or using the BriefCase app ("BriefCase"), you agree to be bound by these Terms and Conditions. If you do not agree to these terms, you may not access or use BriefCase.
Use of BriefCase
You may use BriefCase only for lawful purposes and in accordance with these Terms and Conditions. You agree not to use BriefCase: In any way that violates any applicable federal, state, local, or international law or regulation. To upload, transmit, or otherwise make available any material that is unlawful, harmful, threatening, abusive, harassing, tortious, defamatory, vulgar, obscene, libelous, invasive of another's privacy, hateful, or racially, ethnically, or otherwise objectionable.   To impersonate any person or entity, or falsely state or otherwise misrepresent your affiliation with a person or entity. To interfere with or disrupt the operation of BriefCase or the servers or networks connected to BriefCase, or disobey any requirements, procedures, policies, or regulations of networks connected to BriefCase.  
Content
You may provide input to our Services (“Input”) and receive output based on that Input (“Output”). Collectively, Input and Output are referred to as “Content.” You are solely responsible for any content that you upload, transmit, or otherwise make available through BriefCase ("User Content"). You are responsible for ensuring that your Content complies with all applicable laws and these Terms. You represent and warrant that you have all necessary rights, licenses, and permissions to provide Content to our Services. All User Content is publicly available material and does not contain any confidential or proprietary information.
Users must ensure that their Content does not infringe on third-party intellectual property rights. Luri, Inc. is not liable for any claims arising from Content provided by users.
We operate under the principle of transformative fair use, allowing the use of copyrighted material in ways that add new expression or meaning. By using our Services, you acknowledge and accept these responsibilities and protections related to user-generated Content.


Ownership of Content: As between you and Luri, Inc., and to the extent permitted by applicable law, you (a) retain ownership rights in Input, and (b) own the Output. We hereby assign to you all our right, title, and interest, if any, in and to Output.
Similarity of Content: Due to the nature of our Services and artificial intelligence, Output may not be unique, and other users may receive similar Output. Our assignment of rights does not extend to Output generated by other users or any Third Party Output.
Our Use of Content: We may use Content to provide, maintain, develop, and improve our Services, comply with applicable laws, enforce our terms and policies, and ensure the safety and functionality of our Services.
Accuracy: Artificial intelligence and machine learning are evolving fields. We continuously work to improve our Services for accuracy, reliability, safety, and benefit. Due to the probabilistic nature of machine learning, Output may sometimes not accurately reflect real people, places, or facts.
When using our Services, you understand and agree:
Output may not always be accurate. Do not rely solely on Output from our Services for factual information or professional advice.
Evaluate Output for accuracy and appropriateness for your use case, including human review as needed, before using or sharing Output.
Do not use Output related to individuals for purposes that could significantly impact them, such as making important decisions about credit, education, employment, housing, insurance, legal, or medical matters.
Our Services may produce incomplete, incorrect, or offensive Output that does not represent the views of Luri, Inc. References to third-party products or services do not imply endorsement or affiliation with Luri, Inc.
Non-Infringing Use: Luri, Inc. respects intellectual property rights and employs measures to mitigate risks associated with copyright infringement. Our defenses include:
User-Generated Material: Users are responsible for ensuring that their Content does not infringe on third-party intellectual property rights. We are not liable for any claims arising from Content provided by users.
Publicly Available Data: Our platform may use data publicly available or licensed by users. We are not responsible for any copyright infringement claims related to such data.
Transformative Fair Use: We may rely on defenses such as transformative fair use under copyright law, which allows for the use of copyrighted material in a manner that adds new expression or meaning.
Substantial Similarity: We will defend against claims based on substantial similarity by demonstrating that the Output generated does not infringe on existing copyrights or intellectual property rights.
By using our Services, you acknowledge and accept these terms related to Content and intellectual property protections.
Disclaimer of Warranties
BriefCase is provided on an "as is" and "as available" basis. We make no representations or warranties of any kind, express or implied, as to the operation of BriefCase or the information, content, materials, or products included on BriefCase.   You expressly agree that your use of BriefCase is at your sole risk.
Limitation of Liability
We shall not be liable for any damages of any kind arising from the use of BriefCase, including, but not limited to, direct, indirect, incidental, punitive, and consequential damages. 
6. Indemnification
You agree to indemnify, defend, and hold harmless us, our affiliates, officers, directors, employees, agents, and licensors from and against any and all claims, liabilities, damages, losses, costs, expenses, or fees (including reasonable attorneys' fees) arising from your use of BriefCase or your violation of these Terms and Conditions.   
7. Billing Services
We use Stripe to process payments for BriefCase. By using BriefCase, you agree to be bound by Stripe's terms of service. You agree to pay all fees and charges incurred in connection with your use of BriefCase, including any applicable taxes.
Customer Responsibility for Subscription Costs: By subscribing to our service, you agree to pay all associated subscription costs as outlined at the time of purchase. It is your responsibility to ensure that your payment information is accurate and up-to-date.
Renewal and Billing: Subscriptions are billed on a recurring basis according to the plan you selected (e.g., monthly). Renewal charges will be automatically applied to your payment method on the renewal date of your subscription. It is your responsibility to review and understand the billing cycle of your subscription plan.
Cancellation and Non-Refund Policy: To avoid incurring additional charges, you must cancel your subscription before the next billing cycle begins. You can cancel your subscription through your account settings on our website. We do not provide refunds for any subscription charges that have already been processed.
Failure to Cancel: If you do not cancel your subscription prior to the renewal date, you will be billed for the upcoming billing cycle. You remain liable for all charges incurred as a result of continued subscription until you successfully cancel your subscription.
No Liability for Charges: We are not responsible for any costs or charges incurred due to failure to cancel your subscription in a timely manner. It is your sole responsibility to manage and cancel your subscription if you no longer wish to continue using our service.
By using our service, you acknowledge and accept these terms regarding subscription renewal and cancellation responsibilities.
8. Confidentiality
We will treat any personally identifiable information that you provide through BriefCase in accordance with our Privacy Policy. You agree not to disclose any confidential information obtained through BriefCase to any third party without our prior written consent.
9. Modifications to BriefCase
We reserve the right to modify or discontinue, temporarily or permanently, BriefCase or any part thereof with or without notice. You agree that we shall not be liable to you or to any third party for any modification, suspension, or discontinuance of BriefCase.  


10. Dispute Resolution
  
YOU AND LURI, INC. AGREE TO THE FOLLOWING MANDATORY ARBITRATION AND CLASS ACTION WAIVER PROVISIONS:
Mandatory Arbitration: You and Luri, Inc. agree to resolve any claims arising out of or relating to these Terms or our Services, regardless of when the claim arose, even if it was before these Terms existed (a “Dispute”), through final and binding arbitration. You may opt out of arbitration within 30 days of account creation or any updates to these arbitration terms by filling out this form (opens in a new window). If you opt out of an update, the last set of agreed-upon arbitration terms will apply.
Informal Dispute Resolution: We prefer to address your concerns before formal legal action. Before either party files a claim, we agree to attempt to resolve the Dispute informally. You agree to send us notice through this form (opens in a new window), and we will send notice to the email address associated with your account. If we cannot resolve the Dispute within 60 days, either party may initiate arbitration. We also agree to attend an individual settlement conference if requested by either party during this time. Any statute of limitations will be paused during this informal resolution process.
Arbitration Forum: If the Dispute remains unresolved, either party may commence arbitration with National Arbitration and Mediation (“NAM”) under its Comprehensive Dispute Resolution Rules and Procedures and/or Supplemental Rules for Mass Arbitration Filings, as applicable (available here (opens in a new window)). Luri, Inc. will not seek attorneys’ fees and costs in arbitration unless the arbitrator finds your claim to be frivolous. The Federal Arbitration Act will govern the interpretation and enforcement of these arbitration terms and any arbitration.
Arbitration Procedures: Arbitration will be conducted by videoconference if possible. If the arbitrator determines an in-person hearing is necessary, the location will be mutually agreed upon, in the county where you reside, or as determined by the arbitrator, unless the batch arbitration process applies. The arbitration will be conducted by a sole arbitrator, either a retired judge or an attorney licensed to practice law in California. The arbitrator will have exclusive authority to resolve any Dispute, except state or federal courts in San Francisco, California, have authority to determine enforceability, validity of the class action waiver, or requests for public injunctive relief. Settlement offers will not be disclosed to the arbitrator until after the final award is determined. The arbitrator has the authority to grant motions dispositive of all or part of any Dispute.
Exception: This section does not require informal dispute resolution or arbitration for the following claims: (i) individual claims brought in small claims court; and (ii) injunctive or other equitable relief to stop unauthorized use or abuse of the Services or intellectual property infringement or misappropriation.
Class and Jury Trial Waivers: You and Luri, Inc. agree that Disputes must be brought on an individual basis only and may not be brought as a plaintiff or class member in any purported class, consolidated, or representative proceeding. Class arbitrations, class actions, and representative actions are prohibited. Only individual relief is available. The parties agree to sever and litigate in court any request for public injunctive relief after completing arbitration for the underlying claim and all other claims. This does not prevent either party from participating in a class-wide settlement. You and Luri, Inc. knowingly and irrevocably waive any right to trial by jury in any action, proceeding, or counterclaim.
Batch Arbitration: If 25 or more claimants represented by the same or similar counsel file demands for arbitration raising substantially similar Disputes within 90 days of each other, you and Luri, Inc. agree that NAM will administer them in batches of up to 50 claimants each (“Batch”), unless there are fewer than 50 claimants in total or after batching, which will comprise a single Batch. NAM will administer each Batch as a single consolidated arbitration with one arbitrator, one set of arbitration fees, and one hearing held by videoconference or in a location decided by the arbitrator for each Batch. If any part of this section is found to be invalid or unenforceable for a particular claimant or Batch, it will be severed and arbitrated in individual proceedings.
Severability: If any part of these arbitration terms is found to be illegal or unenforceable, the remainder will remain in effect, except if a finding of partial illegality or unenforceability would allow class arbitration, class action, or representative action, this entire dispute resolution section will be unenforceable in its entirety.
11. Governing Law
These Terms and Conditions shall be governed by and construed in accordance with the laws of the State of California, without giving effect to any principles of conflicts of law.   
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
page = st.sidebar.radio("Go to", ("Monthly Subscription", "Annual Subscription", "Review our Terms & Conditions"))

# First Subscription option 
if page == "Annual Subscription":
    st.title("Renew your BriefCase subscription once a year")
    st.subheader("Follow us on Instagram and comment LURI.AI on any of our posts for a promo code for 2 free weeks of BriefCase!")
    with st.expander("View & Confirm Agreement"):
        with st.container(height=300):  # Create a scrollable container
            st.markdown(terms_and_conditions)

    if st.checkbox("I agree to the Terms and Conditions", value=terms_state):
            terms_state = True

     # Show the modal with the legal terms when the terms button is clicked
    if terms_state:
       confirm_button = st.button("Confirm & Pay", disabled=not terms_state)
        # Show the modal with the legal terms when the terms button is clicked
       if confirm_button:
            terms_state = False
            stripe_js_annual = """
            <script async src="https://js.stripe.com/v3/buy-button.js"></script>
            <stripe-buy-button
            buy-button-id="buy_btn_1Pmld7BqWfU9o3QlYb7IJn04"	
            publishable-key="pk_live_51PmkRJBqWfU9o3Ql8aJH7gsPYqjWE7BvMU2pQpjyrfcsGEyFFbpDZt7yBiKbPwDYc4x2e2Tyx7KulO4VjsfoKDM400QrGD3Ylj"
            ></stripe-buy-button>
            """.format(stripe_publishable_key)
            # user next steps for payment
            st.write("Thanks for confirming the terms and conditions!") 
            st.write("Once your payment has been processed you will receive a link to BriefCase by 9 am PST the following day. The BriefCase link will be emailed to the email address you associated with your subscription.")
            st.write("Please note that you will only be able to access BriefCase while logged into the email you provide for payment. If you'd like to link a different email to BriefCase instead, please contact support@luri.ai.")
            st.components.v1.html(stripe_js_annual, height=400)
        

# Second subscription option 
elif page == "Monthly Subscription":
    st.title("Renew your BriefCase subscription on a monthly basis:")
    st.subheader("Follow us on Instagram and comment LURI.AI on any of our posts for a promo code for 2 free weeks of BriefCase!")
    with st.expander("View & Confirm Agreement"):
        with st.container(height=300):  # Create a scrollable container
            st.markdown(terms_and_conditions)
    if st.checkbox("I agree to the Terms and Conditions", value=terms_state):
            terms_state = True

     # Show the modal with the legal terms when the terms button is clicked
    if terms_state:
       confirm_button = st.button("Confirm & Pay", disabled=not terms_state)
        # Show the modal with the legal terms when the terms button is clicked
       if confirm_button:
          terms_state = False
          stripe_js_monthly = """
          <script async src="https://js.stripe.com/v3/buy-button.js"></script>
          <stripe-buy-button
          buy-button-id="buy_btn_1PmkwhBqWfU9o3QlQwEd8Nso"
          publishable-key="pk_live_51PmkRJBqWfU9o3Ql8aJH7gsPYqjWE7BvMU2pQpjyrfcsGEyFFbpDZt7yBiKbPwDYc4x2e2Tyx7KulO4VjsfoKDM400QrGD3Ylj"
          ></stripe-buy-button>
          """.format(stripe_publishable_key)
          # user next steps for payment
          st.write("Thanks for confirming the terms and conditions!")
          st.write("Once your payment has been processed you will receive a link to BriefCase by 9 am PST the following day. The BriefCase link will be emailed to the email address you associated with your subscription.")
          st.write("Please note that you will only be able to access BriefCase while logged into the email you provide for payment. If you'd like to link a different email to BriefCase instead, please contact support@luri.ai.")
          st.components.v1.html(stripe_js_monthly, height=400)
            #st.image("beach_payment.png", caption="Scan the QR code to pay")
            #url = "https://mainnet.demo.btcpayserver.org/api/v1/invoices?storeId=4r8DKKKMkxGPVKcW9TXB2eta7PTVzzs192TWM3KuY52e&price=100&currency=USD&defaultPaymentMethod=BTC"
            #link='Pay wit BTC [via this link](https://mainnet.demo.btcpayserver.org/api/v1/invoices?storeId=4r8DKKKMkxGPVKcW9TXB2eta7PTVzzs192TWM3KuY52e&price=100&currency=USD&defaultPaymentMethod=BTC)'
            #st.markdown(link,unsafe_allow_html=True)
            #components.iframe(url,width = 300,height = 500, scrolling=True)
   
# Terms & Conditions page
if page == "Review our Terms & Conditions":
        st.info(terms_and_conditions)
