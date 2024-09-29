# from django.conf import settings
# from django.core.mail import send_mail
# from celery import shared_task



# @shared_task
# def send_otp_email(email, otp_code):
#     subject = 'Your OTP code'
#     message = f'Your OTP code is: {otp_code}'
#     from_email = settings.DEFAULT_FROM_EMAIL
#     recipient_list = [email]

#     try:
#         send_mail(subject, message, from_email, recipient_list)
#         return f'Email sent to {email}'
    
#     except Exception as e:
#         return False


import logging
from django.conf import settings
from celery import shared_task
from django.core.mail import send_mail
logger = logging.getLogger(__name__)

@shared_task
def send_otp_email(email, otp_code):
    subject = 'Your OTP Code'
    message = f'Your OTP code is {otp_code}.'
    from_email = settings.DEFAULT_FROM_EMAIL  # Ensure this is set correctly
    recipient_list = [email]

    try:
        logger.info(f"Sending email to {email} with OTP {otp_code}")
        send_mail(subject, message, from_email, recipient_list)
        logger.info(f"Email Successfully sent to {email}")
        return f"Email sent to {email}"

    except Exception as e:
        logger.info(f"Error sending email to {email}: {str(e)}")
        return f"Error sending email to {email}: {str(e)}"
