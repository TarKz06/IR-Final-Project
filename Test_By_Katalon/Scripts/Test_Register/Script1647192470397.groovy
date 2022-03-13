import static com.kms.katalon.core.checkpoint.CheckpointFactory.findCheckpoint
import static com.kms.katalon.core.testcase.TestCaseFactory.findTestCase
import static com.kms.katalon.core.testdata.TestDataFactory.findTestData
import static com.kms.katalon.core.testobject.ObjectRepository.findTestObject
import static com.kms.katalon.core.testobject.ObjectRepository.findWindowsObject
import com.kms.katalon.core.checkpoint.Checkpoint as Checkpoint
import com.kms.katalon.core.cucumber.keyword.CucumberBuiltinKeywords as CucumberKW
import com.kms.katalon.core.mobile.keyword.MobileBuiltInKeywords as Mobile
import com.kms.katalon.core.model.FailureHandling as FailureHandling
import com.kms.katalon.core.testcase.TestCase as TestCase
import com.kms.katalon.core.testdata.TestData as TestData
import com.kms.katalon.core.testng.keyword.TestNGBuiltinKeywords as TestNGKW
import com.kms.katalon.core.testobject.TestObject as TestObject
import com.kms.katalon.core.webservice.keyword.WSBuiltInKeywords as WS
import com.kms.katalon.core.webui.keyword.WebUiBuiltInKeywords as WebUI
import com.kms.katalon.core.windows.keyword.WindowsBuiltinKeywords as Windows
import internal.GlobalVariable as GlobalVariable
import org.openqa.selenium.Keys as Keys

WebUI.openBrowser('')

WebUI.navigateToUrl('http://127.0.0.1:5000/')

WebUI.click(findTestObject('Object Repository/Page_Flask Auth Example/a_Sign Up (1)'))

WebUI.setText(findTestObject('Object Repository/Page_Flask Auth Example/input_Your email_email (6)'), 'prin@gmail.com')

WebUI.setText(findTestObject('Object Repository/Page_Flask Auth Example/input_Your name_name (1)'), 'pluk')

WebUI.setEncryptedText(findTestObject('Object Repository/Page_Flask Auth Example/input_Your password_password (6)'), 'iGDxf8hSRT4=')

WebUI.setEncryptedText(findTestObject('Object Repository/Page_Flask Auth Example/input_Your re-password_re-password (1)'), 
    'iGDxf8hSRT4=')

WebUI.click(findTestObject('Object Repository/Page_Flask Auth Example/button_Sign Up (1)'))

WebUI.closeBrowser()

WebUI.openBrowser('')

WebUI.navigateToUrl('http://127.0.0.1:5000/')

WebUI.click(findTestObject('Object Repository/Page_Flask Auth Example/a_Sign Up (1)'))

WebUI.setText(findTestObject('Object Repository/Page_Flask Auth Example/input_Your email_email (6)'), 'prin2814@gmail.com')

WebUI.setText(findTestObject('Object Repository/Page_Flask Auth Example/input_Your name_name (1)'), 'plook')

WebUI.setEncryptedText(findTestObject('Object Repository/Page_Flask Auth Example/input_Your password_password (6)'), 'rW9vhuzPudMFJ91kzAKOCA==')

WebUI.setEncryptedText(findTestObject('Object Repository/Page_Flask Auth Example/input_Your re-password_re-password (1)'), 
    'rW9vhuzPudMFJ91kzAKOCA==')

WebUI.click(findTestObject('Object Repository/Page_Flask Auth Example/button_Sign Up (1)'))

WebUI.click(findTestObject('Object Repository/Page_Flask Auth Example/a_Sign Up (1)'))

WebUI.setText(findTestObject('Object Repository/Page_Flask Auth Example/input_Your email_email (6)'), 'pluk@gmail.com')

WebUI.setText(findTestObject('Object Repository/Page_Flask Auth Example/input_Your name_name (1)'), 'prin')

WebUI.setEncryptedText(findTestObject('Object Repository/Page_Flask Auth Example/input_Your password_password (6)'), 'rW9vhuzPudMFJ91kzAKOCA==')

WebUI.setEncryptedText(findTestObject('Object Repository/Page_Flask Auth Example/input_Your re-password_re-password (1)'), 
    'rW9vhuzPudMFJ91kzAKOCA==')

WebUI.click(findTestObject('Object Repository/Page_Flask Auth Example/button_Sign Up (1)'))

WebUI.closeBrowser()

