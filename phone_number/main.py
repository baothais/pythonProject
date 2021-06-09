import phonenumbers
from phonenumbers import geocoder
from phonenumbers import carrier

def phone_number():
    number = "+84905125206"
    vi_number = phonenumbers.parse(number)
    print(geocoder.description_for_number(vi_number, "en"))

    service_number = phonenumbers.parse(number)
    print(carrier.name_for_number(service_number, "en"))

if __name__=="__main__":

    phone_number()


