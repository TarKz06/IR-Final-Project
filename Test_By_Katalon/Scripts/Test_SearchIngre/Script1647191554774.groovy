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

WebUI.click(findTestObject('Object Repository/Page_Flask Auth Example/a_Login (3)'))

WebUI.setText(findTestObject('Object Repository/Page_Flask Auth Example/input_Your email_email (4)'), 'prin@gmail.com')

WebUI.setEncryptedText(findTestObject('Object Repository/Page_Flask Auth Example/input_Your password_password (4)'), 'iGDxf8hSRT4=')

WebUI.click(findTestObject('Object Repository/Page_Flask Auth Example/input_Your password_remember (3)'))

WebUI.click(findTestObject('Object Repository/Page_Flask Auth Example/button_Login to your account (3)'))

WebUI.click(findTestObject('Object Repository/Page_Flask Auth Example/a_home (1)'))

WebUI.click(findTestObject('Object Repository/Page_Flask Auth Example/button_Search by Food ingredient'))

WebUI.setText(findTestObject('Object Repository/Page_Flask Auth Example/input_Find your DISH_inputword (1)'), 'love')

WebUI.click(findTestObject('Object Repository/Page_Flask Auth Example/button_search (1)'))

WebUI.closeBrowser()

