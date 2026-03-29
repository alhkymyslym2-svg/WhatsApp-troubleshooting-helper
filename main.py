from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
from kivymd.uix.button import MDRaisedButton
from kivymd.uix.toolbar import MDTopAppBar
from kivymd.uix.label import MDLabel
import webbrowser

class WhatsAppHelper(MDApp):
    def build(self):
        # اختيار ألوان الواتساب الرسمية
        self.theme_cls.primary_palette = "Teal" 
        self.theme_cls.primary_hue = "800"
        
        screen = MDScreen()
        
        # الشريط العلوي
        toolbar = MDTopAppBar(
            title="مساعد فك حظر واتساب", 
            pos_hint={"top": 1},
            elevation=4
        )
        
        # نص توضيحي
        label = MDLabel(
            text="إذا تم حظر حسابك، اضغط على الزر أدناه\nللتواصل مباشرة مع فريق دعم واتساب الرسمي:",
            halign="center",
            theme_text_color="Secondary",
            font_style="Subtitle1",
            pos_hint={"center_y": 0.7}
        )
        
        # زر "فك الحظر" الاحترافي
        btn = MDRaisedButton(
            text="إرسال طلب فك الحظر الآن",
            pos_hint={"center_x": 0.5, "center_y": 0.45},
            size_hint=(0.8, 0.08),
            md_bg_color=(0.02, 0.4, 0.35, 1), # لون أخضر واتساب
            on_release=self.contact_support
        )
        
        screen.add_widget(toolbar)
        screen.add_widget(label)
        screen.add_widget(btn)
        return screen

    def contact_support(self, instance):
        # هذا الرابط يفتح صفحة دعم واتساب الرسمية مباشرة
        # أو يمكنك تغييره لفتح إيميل (mailto:support@whatsapp.com)
        support_url = "https://www.whatsapp.com/contact/?subject=messenger"
        webbrowser.open(support_url)

if __name__ == "__main__":
    WhatsAppHelper().run()
