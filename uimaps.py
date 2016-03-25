loginpagemap = dict(
    
SignInTabXpath = "//li/a[contains(text(),'Sign In')]",
LogInH1Xpath = "//h1[text()='Login']",
CookieAlertXpath = "//a[@class = 'cc_btn cc_btn_accept_all']",
LogInFormDivXpath = "//h2[contains(text(),'Login using email and password')]",
LogInFormEmailXpath ="//input[@name = 'email']",
LogInFormPasswordXpath = "//input[@name = 'password']",
LogInFormSubmitXpath ="//button[contains(text(),'Login')]",
LogInFormAccountTabXpath = "//span[text()='Account']",
LogInLogoutButtonXpath = "//a[contains(text(),'Logout')]",
LogInFacebookXpath = "//span[contains(text(),'Login with Facebook')]",
LogInFacebookUsernameXpath = "//input[@id='email']",
LogInFacebookPasswordXpath = "//input[@id='pass']",
LogInFacebookLoginXpath = "//input[@name='login']",


)

signuppagemap = dict(
    
SignUpTabXpath = "//li/a[text()='Sign Up']",
CookieAlertXpath = "//a[@class = 'cc_btn cc_btn_accept_all']",
SignUpEmailXapth = "//span[contains(text(),'Login using email and password')]",
SignUpEmailUsernameXpath = "//input[contains(@name,'username')]",
SignUpEmailEmailXpath = "//input[contains(@name,'email')]",
SignUpEmailPasswordXpath = "//input[contains(@name,'password')]",
SignUpEmailPasswordConfirmXpath = "//input[contains(@name,'password_confirmation')]",
SignUpEmailSubmitXpath = "//button[contains(text(),'Register')]",
SignUpEmailAccountTabXpath = "//span[text()='Account']",
SignUpFacebookXpath = "//span[contains(text(),'Login with Facebook')]",
SignUpFacebookUsernameXpath = "//input[@id='email']",
SignUpFacebookPasswordXpath = "//input[@id='pass']",
SignUpFacebookLoginXpath = "//input[@name='login']",
SignUpFacebookAccountTabXpath = "//span[text()='Account']",

)

startuppagemap = dict(
    
StartUpPageSignInTabXpath = "//li/a[contains(text(),'Sign In')]",

)

createofferpagemap = dict(
    
#############BASIC Details Tab ################
FindRoommateTabXpath = "//span[contains(text(),'Find Roommates')]",
CreateOfferTabXpath = "//a[contains(text(),'Create Offer')]",
CreateOfferAddressXpath = "//h2[contains(text(),'Address')]",
CreateOfferInputAddressXpath = "//input[@placeholder = 'Address']",
CreateOfferInputFloorXpath ="//select[@name = 'floor']",
CreateOfferInputFloorOptionXpath ="(//select[@name = 'floor']//option)[3]",

#For Room data fill up
CreateOfferSharedFlatXpath = "//button[contains(text(),'Shared Flat')]",
CreateOfferRoomFreeFromXpath ="//span[contains(text(),'Free from')]/ancestor::label/following-sibling::input[1]",
CreateOfferRoomFreeFromDaterSelectXpath ="//table[@class = 'ui-datepicker-calendar']//td/a[contains(text(),'{0}')]",
CreateOfferRoomSizeXpath ="//input[@name = 'room_size']",
CreateOfferRoommatesXpath = "//select[@name = 'roommates']",
CreateOfferRoommatesOptionXpath = "(//select[@name = 'roommates']//option)[3]",
CreateOfferRoomFemaleXpath = "//select[@name = 'roommates_female']",
CreateOfferRoomFemaleOptionXpath = "//select[@name = 'roommates_female']",
CreateOfferRoomMaleXpath = "//select[@name = 'roommates_male']",
CreateOfferRoomMaleOptionXpath = "(//select[@name = 'roommates_male']//option)[3]",
CreateOfferRoomFreeToXpath ="//span[contains(text(),'Free until')]/ancestor::label/following-sibling::input[1]",
CreateOfferRoomFreeToDaterSelectXpath ="//table[@class = 'ui-datepicker-calendar']//td/a[contains(text(),'{0}')]",
CreateOfferRoomRentXpath ="//input[@name = 'rent']",

#For Flat data fill up
CreateOfferApartmentXpath = "//button[contains(text(),'Apartment')]",
CreateOfferFlatFreeFromXpath ="//span[contains(text(),'Free from')]/ancestor::label/following-sibling::input[1]",
CreateOfferFlatFreeFromDaterSelectXpath ="//table[@class = 'ui-datepicker-calendar']//td/a[contains(text(),'{0}')]",
CreateOfferFlatSizeXpath ="//input[@name = 'flat_size']",
CreateOfferFlatRoomCountSizeXpath ="//input[@name = 'room_count']",
CreateOfferFlatFreeToXpath ="//span[contains(text(),'Free until')]/ancestor::label/following-sibling::input[1]",
CreateOfferFlatFreeToDaterSelectXpath ="//table[@class = 'ui-datepicker-calendar']//td/a[contains(text(),'{0}')]",
CreateOfferFlatRentXpath = "//input[@name = 'rent']",

#For Next button and wait for element
CreateOfferNextStepBasicDetailsTabXpath = "//button[contains(text(), 'Next Step')]",
CreateOfferNextStepWaitXpath = "//h2[contains(text(),'Offer questions')]",


#############Description Tab ################
CreateOfferOfferTitleXpath = "//div[@class = 'form-group form-group-depth-1']//input[@name='title']",
CreateOfferOfferLocationDescriptionXpath = "//div[@class = 'tab-content']//textarea[@name='description_location']",

CreateOfferOfferRoomTabXpath = "//li/a[text()='Room']",
CreateOfferOfferRoomDescriptionXpath = "//div[@class = 'form-group form-group-depth-1']/following-sibling::div[1]//textarea[@name='description_room']",

CreateOfferOfferFlatLifeTabXpath = "//li/a[text()='Flat life']",
CreateOfferOfferFlatLifeDescriptionXpath = "//div[@class = 'form-group form-group-depth-1']/following-sibling::div[1]//textarea[@name='description_flat_life']",

CreateOfferOfferLookingForTabXpath = "//li/a[text()='Looking for']",
CreateOfferOfferLookingForDescriptionXpath = "//div[@class = 'form-group form-group-depth-1']/following-sibling::div[1]//textarea[@name='description_looking_for']",

CreateOfferOfferHigkLights1Xpath = "(//div[@class = 'col-md-8']//input)[1]",
CreateOfferOfferHigkLights2Xpath = "(//div[@class = 'col-md-8']//input)[2]",
CreateOfferOfferHigkLights3Xpath = "(//div[@class = 'col-md-8']//input)[3]",

CreateOfferNextStepDescriptionTabTabXpath = "//button[contains(text(), 'Next Step')]",


#############Looking For Tab ################
CreateOfferOfferSmokingXpath="//select[@name='smoking']",
CreateOfferOfferSmokingOptionXpath="(//select[@name='smoking']//option)[2]",

CreateOfferOfferAgeBetweenXpath= "//input[@name='age_min']",

CreateOfferOfferLookingForXpath="//select[@name='looking_for_gender']",
CreateOfferOfferLookingForOptionXpath="(//select[@name='looking_for_gender']//option)[2]",

CreateOfferOfferUndXpath="//input[@name='age_max']",


CreateOfferOfferQuestion1Xpath="//input[@label='Question 1']",
CreateOfferOfferQuestion2Xpath="//input[@label='Question 2']",
CreateOfferOfferQuestion3Xpath="//input[@label='Question 3']",

CreateOfferNextStepLookinForTabTabXpath = "//button[contains(text(), 'Next Step')]",


#############Images Tab ################

CreateOfferOfferImageXpath="//input[@type = 'file']",
CreateOfferOfferImageWaitElementXpath="//a[@class='fancybox-thumb thumbnail']",

CreateOfferOfferDoneXpath="//button[contains(text(), 'Done!')]",
CreateOfferOfferDoneWaitElementXpath="//div[@id='tabs-list']",

)