import sys
sys.dont_write_bytecode = True

general_constants = dict(
    browser = 'chrome',
    base_url = 'http://wgcast:7JxwZkCwK@wgcast2013.webfactional.com/'
)


class StartPageConstants(object):
    base_page_constants = dict(
        search_city_text = 'Berlin, Deutschland', 
    )


class LogInPageConstants(object):
    login_constants = dict(
        username = 'testuser@yahoo.com',
        password = '1234'    
    )
    
    faceebook_login_constants = dict(
        username = 'msi_g@yahoo.com',
        password = '1234'    
    )


class SignUpPageConstants(object):
    login_constants = dict(
        username = 'itistester',
        email = 'itistester@yahoo.com',
        password = '12345'    
    )
    
    faceebook_login_constants = dict(
        username = 'msi_g@yahoo.com',
        password = '1234'    
    )

class CreateOfferConstants(object):
    
    create_offer_basicdetails_constants = dict(
        address = "Europaplatz 1, Berlin, Mitte, 10557 ",
        district = 'Mitte',
        floor = '2',
        select_from_data = '11',
        room_size = '1200',
        number_roommates = '3',
        number_female = '2',
        number_male = '2',
        select_to_data = '11',
        room_rent = '2500',
    )
    
    create_offer_description_constants = dict(
        title = "My test Title",
        location_description = 'My location description',
        room_description = 'My room description',
        flatlife_description = 'My flatlife description',
        lookingfor_description = 'My lookingfor description',
    )
    
    create_offer_highlights_constants = dict(
        speciality_one = "speciality_one",
        speciality_two = "speciality_two",
        speciality_three = "speciality_three",
    
    )
    
    create_offer_lookingfor_constants = dict(
        smoking = "allowed",
        age_between = '16-30',
        looking_for = 'Male',
        und = 'What more!',
    )
    
    create_offer_questions_constants = dict(
        question_one = "question_one",
        question_two = "question_two",
        question_three = "question_three",
    )
    create_offer_uploadimage_constants = dict(
        image_path = r"C:\Users\Winrock\Desktop\SCRPROJ\SleniumTesting\2.jpg"
    )



class locators:
    ID='id'
    NAME = 'name'
    XPATH = 'xpath'
    CSS_SELECTOR = 'cssSelector'
