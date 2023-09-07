from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.factory import Factory
from kivymd.uix.bottomsheet import MDCustomBottomSheet
from kivy.uix.boxlayout import BoxLayout
from kivy_garden.mapview import MapView,MapMarkerPopup
from kivy.lang import Builder
import webbrowser
from kivymd.uix.button import MDFloatingActionButtonSpeedDial
from payment1 import url


Window.size = (400,600)

func="""

ScreenManager:
    HomeScreen:
    ListScreen:
    
    

<HomeScreen>:
    name:'home1'
    
    	
    	
    	
	MDScrollView:
		MDBoxLayout:
			spacing:2
			orientation: 'vertical'
			size_hint_y: 1.6
			md_bg_color:"white"
			MDBoxLayout:
				padding:10
				spacing:2
				size_hint_y:0.25
				md_bg_color:"orange"

				MDTextField:
					size_hint_x:0.4
					mode:"fill"
					hint_text:"Click Search"
					background_color: "white"
					
					

				MDIconButton:
			        icon:"magnify"
			        theme_icon_color: "Custom"
					icon_color:"white"
					on_release:root.manager.current="ListScreen"
					
					





				MDIconButton:
					icon:"camera"
					theme_icon_color: "Custom"
					icon_color:"white"




				MDIconButton:
					icon:"store-outline"
					theme_icon_color: "Custom"
					icon_color:"white"

			# NOW CREATE CAROUSEL IMAGE 
			MDScrollView:
				# FOR DISABLE y AXIS SCROLL
				do_scroll_y:False
				MDBoxLayout:
					pos_hint_y:'0.7'
				    spacing:5
				    padding:1.5
					# SET WIDTH OF YOU BOX
					size_hint_x:3
					FitImage:
						source:"now-open-shop-new-store-2093114.jpg"
						
						
					FitImage:
						source:"image3.jpg"
					FitImage:
						source:"image1.png"
			# CREATE ICON MENU LIKE SHOP OR BALANCE
			


			MDBoxLayout:
				md_bg_color:"white"
				size_hint_y:0.3
				padding:10
				spacing:2
				MDBoxLayout:
					spacing:12
					orientation:"vertical"

					# CREATE 6 ICON
					
					
					MDIconButton:
						icon:"qrcode-scan"
						color:"#D1553E"
						# AND SET SIZE OF ICON
						font_size: 30
						pos_hint:{"center_x":0.5}
						on_release:app.show_qrcode()

					MDLabel:
						text:"   Nearby"
						color:"grey"
						font_size:11
						halign:"center"
				MDBoxLayout:
					md_bg_color:"white"
					spacing:12
					orientation:"vertical"

					# CREATE 6 ICON
					MDIcon:
						icon:"apps"
						color:"#15A190"
						# AND SET SIZE OF ICON
						font_size: 30
						pos_hint:{"center_x":0.5}

					MDLabel:
						text:"Apps"
						color:"grey"
						font_size:13
						halign:"center"

				MDBoxLayout:
					md_bg_color:"white"
					spacing:12
					orientation:"vertical"

					# CREATE 6 ICON
					MDIcon:
						icon:"basket"
						color:"#C9051C"
						# AND SET SIZE OF ICON
						font_size: 30
						pos_hint:{"center_x":0.5}

					MDLabel:
						text:"Shop"
						color:"grey"
						font_size:13
						halign:"center"

				MDBoxLayout:
					md_bg_color:"white"
					spacing:12
					orientation:"vertical"

					# CREATE 6 ICON
					MDIcon:
						icon:"cart-outline"
						color:"#C9051C"
						# AND SET SIZE OF ICON
						font_size: 30
						pos_hint:{"center_x":0.5}

					MDLabel:
						text:"Shopping"
						color:"grey"
						font_size:13
						halign:"center"

				MDBoxLayout:
					md_bg_color:"white"
					spacing:12
					orientation:"vertical"

					# CREATE 6 ICON
					MDIcon:
						icon:"hanger"
						color:"#449ED0"
						# AND SET SIZE OF ICON
						font_size: 30
						pos_hint:{"center_x":0.5}

					MDLabel:
						text:"Clothes"
						color:"grey"
						font_size:13
						halign:"center"

				MDBoxLayout:
					md_bg_color:"white"
					spacing:12
					orientation:"vertical"

					# CREATE 6 ICON
					MDIcon:
						icon:"account-group"
						color:"#449ED0"
						# AND SET SIZE OF ICON
						font_size: 30
						pos_hint:{"center_x":0.5}

					MDLabel:
						text:"Clothes"
						color:"grey"
						font_size:13
						halign:"center"

			# CREATE IMAGE PROMO

			MDBoxLayout:
				md_bg_color:"white"
				size_hint_y:0.9
				padding:10
				spacing:10
				MDBoxLayout:
					radius:20
					md_bg_color:"#EE4C2E"
					size_hint_x:1.6
					padding:20

					# AND CREATE IMAGE
					FitImage:
						source:"image4.jpg"
				MDBoxLayout:
					md_bg_color:"white"
					radius:20
					md_bg_color:"#EE4C2E"

					padding:20

					# AND CREATE IMAGE
					FitImage:
						source:"image5.jpg"

			# CREATE FLASH SALE TEXT
			MDBoxLayout:
				md_bg_color:"white"
				size_hint_y:0.3
				MDIcon:
					icon:"flash"
					font_size:40
					color:"yellow"
					pos_hint:{"center_y":0.5}

				MDLabel:
					text:"Sale of the day"
					font_size:40
					color:"yellow"
					bold:True
					font_style:"Button"

				

			# CREATE HORIZONTAL SCROLL
			# FOR PRODUCT AND PRICE
			MDScrollView:
				do_scroll_y:False
				do_scroll_x:True

				MDBoxLayout:
					size_hint_x:1.5
					size_hint_y:1
					orientation:"horizontal"
					MDCard:
						size_hint_x:0.3
						elevation:30
						MDBoxLayout:
							orientation:"vertical"
							FitImage:
								source:"hp.png"
								size_hint_y:1.5
								size_hint_x:0.8
								pos_hint:{"center_y":0.47,"center_x":0.5}
							MDLabel:
								text:"$.20"
								color:"orange"
								font_size:30
								halign:"center"
								pos_hint:{"center_y":0.97,"center_x":0.5}
								bold:True
					MDCard:
						size_hint_x:0.3
						elevation:30
						MDBoxLayout:
							orientation:"vertical"
							FitImage:
								source:"hp2.jpg"
								size_hint_y:1.2
								size_hint_x:0.4
								pos_hint:{"center_y":0.47,"center_x":0.5}
							MDLabel:
								text:"$.20"
								color:"orange"
								font_size:30
								halign:"center"
								pos_hint:{"center_y":0.97,"center_x":0.5}
								bold:True


			# CREATE SPACE BOTTOM
			MDBoxLayout:
				md_bg_color:"white"
				orientation:"vertical"
				size_hint_y:0.9

			# NOW LAST CREATE BOTOOM BAR
	MDNavigationLayout:
        ScreenManager:
        
            Screen:
            	
                    
                    
            	
                MDBoxLayout:
					orientation:"horizontal"
					padding:10
					spacing:2
					size_hint_y:0.08
					md_bg_color:"orange"
					
				MDIconButton:
					icon:"account-circle"
					on_release: nav_draw.set_state("open")
					theme_text_color:"Custom"
					text_color:"white"
					pos_hint:{'center_x':0.07,'center_y':0.043}	
					
                    
                    
                MDIconButton:
					icon:"map-marker"
					
					theme_text_color:"Custom"
					text_color:"white"
					pos_hint:{'center_x':0.2,'center_y':0.043}					
								        
				MDIconButton:
					icon:"heart"
					
					theme_text_color:"Custom"
					text_color:"white"
					pos_hint:{'center_x':0.80,'center_y':0.043}	
				MDIconButton:
					icon:"cart-outline"
					
					theme_text_color:"Custom"
					text_color:"white"
					pos_hint:{'center_x':0.93,'center_y':0.043}		
					
				MDFloatingActionButton:
					icon:"qrcode-scan"			
					pos_hint:{'center_x':0.5,'center_y':0.073}
					size_hint:(0.14,0.09)
					md_bg_color:"orange"
					on_release:app.show_qrcode()
			
			               



        MDNavigationDrawer:
            id: nav_draw
			
            BoxLayout:
                orientation:"vertical"
                spacing:2
                padding:2
                Image:
                    source:"download.png"


                ScrollView:
                    MDList:
                        OneLineIconListItem:
                            text:"Settings"
                            IconLeftWidget:
                                icon:"cog"
                        OneLineIconListItem:
                            text:"Logout"
                            IconLeftWidget:
                                icon:"logout"
                                

        
        
<ListScreen>:
    name:"ListScreen"
    MDScrollView:
    	
		MDBoxLayout:
			orientation: 'vertical'
			size_hint_y: 1.6
			MDBoxLayout:
				padding:10
				spacing:2
				size_hint_y:0.3
				md_bg_color:"black"
				MDIconButton:
			        icon:"arrow-left"
			        theme_icon_color: "Custom"
					icon_color:"white"
					on_press:root.manager.current="home1"
				MDTextField:
					size_hint_x:0.4
					mode:"fill"
					hint_text:"Results for " + "shoes"
					background_color: "white"

				MDIconButton:
			        icon:"magnify"
			        theme_icon_color: "Custom"
					icon_color:"white"





				MDIconButton:
					icon:"camera"
					theme_icon_color: "Custom"
					icon_color:"white"




				MDIconButton:
					icon:"store-outline"
					theme_icon_color: "Custom"
					icon_color:"white"
    	
			ScrollView:
				MDGridLayout:
					cols:2
					padding:dp(20)
					spacing:dp(20)
					adaptive_height:True
					ElementCard:
						image:'images/blue.png'
						price:'₹200'
						rate:" 4.5/5"
					ElementCard:
						image:'images/1.png'
						price:'₹350'
						rate:" 5/5"
					ElementCard:
						image:'images/blue.png'
						price:'₹800'
						rate:" 4.5/5"
					ElementCard:
						image:'images/2.png'
						price:'₹150'
						rate:" 3.0/5"
					ElementCard:
						image:'images/yellow.png'
						price:'₹400'
						rate:" 4.0/5"
					ElementCard:
						image:'images/3.png'
						price:'₹450'
						rate:" 3.0/5"
<ContentCustomSheet@MDBoxLayout>:
    orientation: "vertical"
    size_hint_y: None
    height:dp(750)
    image:''
    rate:""
    price:""
    padding:dp(12)
    spacing:dp(6)
    RelativeLayout:
        ElementCard:
            pos_hint:{"x":.05,"y":.5}
            image:root.image
            rate:root.rate
            price:root.price

    MDBoxLayout:
        spacing:dp(5)
        Check:
            selected_color:1,0,0,1
            active:True
            unselected_color:1,0,0,1
            pos_hint: {'center_x': .5, 'center_y': .5}
        Check:
            selected_color:0,0,1,1
            unselected_color:0,0,1,1
            pos_hint: {'center_x': .5, 'center_y': .5}

        Check:
            selected_color:0,1,0,1
            unselected_color:0,1,0,1
            pos_hint: {'center_x': .5, 'center_y': .5}
        Check:
            selected_color:1,1,0,1
            unselected_color:1,1,0,1
            pos_hint: {'center_x': .5, 'center_y': .5}
    MDLabel:
        text:"This product is trending now !!!."
        adaptive_height:True
    MDBoxLayout:
        adaptive_width:True
        MDIconButton:
            icon:'plus'
            pos_hint:{"center_x":.5,"center_y":.5}
        MDLabel:
            text:"1"
            halign:'center'
            valign:'center'
        MDIconButton:
            icon:"minus"
            pos_hint:{"center_x":.5,"center_y":.5}

    MDBoxLayout:
        spacing:dp(8)
        MDRoundFlatIconButton:
            icon:"cart"
            text:"Add to cart"
            size_hint_x:1
        MDRoundFlatIconButton:
            icon:"cards-heart"
            text:"Add to Favourites"
            size_hint_x:1
    MDRaisedButton:
        size_hint_x:1
        text:"Buy Now"
<Check@MDCheckbox>:
    group: 'group'
    radio_icon_normal:"checkbox-blank-circle"
    size_hint: None, None
    size: dp(48), dp(48)

<ElementCard@MDCard>:
    image:''
    rate:''
    price:""
    orientation:'vertical'
    on_release:app.show_custom_bottom_sheet(root.image,root.price,root.rate)
    size_hint_x:.5
    elevation:15
    size_hint_y:None
    md_bg_color:app.theme_cls.primary_color
    height:dp(220)
    padding:dp(25)
    spacing:dp(15)
    radius:[25]
    MDBoxLayout:
        height:dp(120)
        size_hint_y:None
        Image:
            source:root.image

    MDBoxLayout:
        size_hint_y:None
        height:dp(25)
        MDIcon:
            icon:'star'
            theme_text_color:'Custom'
            text_color:1,1,0,1
            halign:"center"
            size_hint_x:.25
            # width:dp(30)
        MDLabel:
            text:root.rate

    MDLabel:
        text:root.price
        font_style:'H5'
        

    
        
        
        

    
    
    
    
    
   


"""



class HomeScreen(MDScreen):
	pass

class ListScreen(MDScreen):
	pass




class MyApp(MDApp):


	def switch_screen(self, screen_name):
		self.screen_manager.current = screen_name
	def show_custom_bottom_sheet(self,image,price,rate):
		bottom_sheet=Factory.ContentCustomSheet()
		bottom_sheet.rate=rate
		bottom_sheet.image=image
		bottom_sheet.price=price
		self.custom_sheet = MDCustomBottomSheet(screen=bottom_sheet)
		self.custom_sheet.open()

	def build(self):
		self.theme_cls.theme_style_switch_animation=False

		return Builder.load_string(func)


		return b
	def show_qrcode(self):
		webbrowser.open(url)
if __name__ == "__main__":
	MyApp().run()

