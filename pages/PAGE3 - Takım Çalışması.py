import streamlit as st
from PIL import Image

def page_3():
    st.title("Takım İle Git&GitHub Kullanımı :face_with_monocle:")
    st.markdown("""
    Bu sayfada yeni başlayan bir ekibin Git&GitHub platformunu nasıl beraber kullanabilecekleri açıklanmaktadır. Hemen bu
    yazının altında bulunan diagram iki kişinin remote repo üzerinde nasıl beraber çalışabilceklerini gösteriyor. Bu
    şekilde çalışabilmek için izlemeniz gereken adımlar aşağıdaki açıklamalarda.
    """)

    image = Image.open('./images/flow.png')
    st.image(image, caption='diagram')

    tab1, tab2, tab3 = st.tabs(["ADIM 1 - Uzak Çalışma Alanı", "ADIM 2 - Yerel Çalışma Alanı", "ADIM 3 - Gönder/Kontrol Et/Birleştir"])

    with tab1:
        step1()
    with tab2:
        step2()
    with tab3:
        step3()

def step1():
    st.markdown("""
**Sanal Dünyada Bir Çalışma Alanı Oluşturun:** Bir ekip ile çalışmaya başlamadan önce ilk olarak çalışmaların yükleneceği 
        ve birleştireleceği ortamı kurmak gereklidir. Bu depo, tüm ekibin projeye erişebileceği ve üzerinde çalışabileceği
         merkezi bir konum sağlar. Remote repo açmak için izlemeniz gereken adımlar :
         
""")
    st.markdown("""
            1. **Git hizmeti sağlayıcısı seçimi:** *Öncelikle, Git hizmeti sağlayıcısı olarak GitHub, GitLab veya Bitbucket gibi popüler 
            platformlardan birini seçmeniz gerekir. Bu platformlar, projelerinizi yönetmek ve takımınızla işbirliği yapmak için gerekli 
            araçları sağlar.*
            2. **Hesap oluşturma:** *Seçtiğiniz Git hizmeti sağlayıcısının web sitesine giderek bir hesap oluşturmanız gerekmektedir. Genellikle, 
            hesap oluşturmak ücretsizdir, ancak bazı ek özellikler için ücretli planlara geçiş yapabilirsiniz.*
            3. **Yeni bir depo oluşturma:** *Hesabınızı oluşturduktan sonra, projenizin yer alacağı yeni bir depo oluşturmanız gerekecektir. 
            Genellikle, "New Repository" veya benzeri bir düğme ile yeni depo oluşturma seçeneği bulunur. Depo oluşturma işlemi sırasında, 
            depo adını, açıklamasını ve gizlilik ayarlarını belirlemeniz istenecektir.*
            4. **Depo ayarları:** *Depo oluşturulduktan sonra, bazı ayarları düzenlemeniz gerekebilir. Örneğin, ekip üyelerini depoya davet 
            etmek, geliştirme sürecini kolaylaştıracak ek özellikleri etkinleştirmek veya depo izinlerini ayarlamak gibi adımları takip 
            etmeniz gerekebilir.*
            5. **İlk kodunuzu gönderme:** *Depo oluşturulduktan sonra, projenizin ilk kodunu göndermek için Git istemcisini kullanabilirsiniz. 
            Git istemcisi, projenizin yerel bir kopyasını oluşturmanızı ve ardından değişiklikleri depoya göndermenizi sağlar. Bu sayede, 
            takımınızla kod paylaşabilir ve projenin güncel bir sürümünü depoda tutabilirsiniz.*
    """)
def step2():
    st.markdown("""
    Bu adıma geçmeden önce bir önceki adımı yaptığınızı varsayıyorum. Artık online bir çalışma alanınız bulunuyor, bu
    çalışma alanını kodlarınızı birleştirmek, takip etmek ve karşılaştırmak için kullanıcaksınız. Ayrıca projenizin en 
    güncel halinide depolayacak. Bir sonraki adım ise bu online çalışma alanı, bundan sonra 'remote repo' olarak bahsedeceğim,
    ile bağlı yerel bir çalışma alanı yani yerekl bir repo kuracağız. Yerel repo'muz herhangi bir çakışma ve uyumsuzluk 
    olmaması için Remote repo'muzun bir klonu (yerel kopyası) olacak. O zaman hemen cmd veya git bash terminalini açın ve
    remote repo'nuzu klonlayın. 
    """)
    st.code("git clone <remote-repo-URL>", language='bash')
    st.markdown("""
    :exclamation: Unutmayın, projenin yerel kopyasında yaptığınız değişiklikler online depoyu etkilemez. Yaptığımız
    çalışmaları git komuları ile remote repo'ya iletmemiz gereklidir. 
    """)

    st.markdown("""
    Bir sonraki adımımız hemen kendi çalışmalarımız için bir dal(branch) oluşturmakta. Bunu yapmaktaki amacımız ilerideki
    çalışmalarımızı remote repo'ya ilettiğimizde var olan dosyaların üstüne yazmaktansa bizim yeni oluşturduğumuz dal(branch)
    şeklinde karşılaştırmada yapabileceğimiz şekilde yükleme yapabilmektedir. Yeni çalışma dalınızı oluşturmak için git
    terminali (git bash) üzeridnen aşağıdaki komutları çalıştırın: 
    """)
    st.code('git branch -M <dal-adı>',language='bash')

    st.markdown("""
    Artık çalışmalarınıza başlayabilrisiniz. Yaptığınız değişiklikleri ve yenilikleri `git add` komutuyla takibe ekleyebilir,
    `git commit` komutuyla da yaptığınız değişiklikleri kayıt edebilirsiniz. Ancak, bu  kayıt ettiğiniz8commit) değişiklikler
    henüz online depoya gönderilmemiş olur.
    """)
    st.code("git add <dosya-adı>", language='bash')
    st.code("git commit -m 'Değişiklik açıklaması'", language='bash')

    st.markdown("""
    Bir sonraki adıma geçmeden önce konuşmamız gerekn bir konu daha var. Yerel reponuz her zaman güncel olmalı. Yani 
    siz kendi değişikliklerinizi remote repo'ya göndermeden önce remote repo'da olan değişikliklerinizi yerel repoya 
    çekmelisiniz. Aksi takdirde remote repo'da kendi orjinal çalışma ile kendi çalımalarımız birleştiriken sorunlar 
    ortaya çaıkabilir. 
    
    Remote repodan çalışmaları çekmek için aşağıdaki komutları kullanabilirsiniz. Remote repo'da ki değişimleri 
    çekmek için benim kişisel tercihim ya çalışmaya başlarken veya çalışmalarınızı göndermeden hemen önce yapılmasıdır.
    """)
    st.code('git pull', language='bash')
    st.markdown("""
    `git pull` komutunu kullanarak diğer ekip üyelerinin yaptığı güncellemeleri alabilir ve yerel çalışma alanınızı güncel tutabilirsiniz. 
     Bu komut, uzaktaki depodaki en son değişiklikleri indirerek yerel kopyanıza entegre eder.
     
     Ayrıca, `git fetch` komutunu da kullanabilirsiniz. `git fetch`, uzaktaki depodaki güncellemeleri indirir, ancak yerel çalışma alanınızı 
     otomatik olarak güncellemez. Yani, `git fetch` ile indirilen güncellemeleri, `git merge` veya `git rebase` gibi komutlarla yerel kopyanıza 
     entegre etmeniz gerekir.
     
     git pull komutu, `git fetch` ve `git merge` işlemlerini birleştirir. Yani, `git pull` komutunu kullanarak hem güncellemeleri 
     indirebilir hem de otomatik olarak yerel çalışma alanınızı güncelleyebilirsiniz.
    """)

def step3():
    st.markdown("""
    Kendi bilgisayarından `git push` işlemini yaptıktan sonra bilgisayarınız ve remote repo'nun bulunduğu platform 
    aralarında çeşitli güvenlik ve uyumluluk testleri yaptıktan sonra bir sorun yok ise çalışmalarınız remote repo'ya 
    yüklenir. Remote repo'nuza girdiğinizde artık sizin remote repo'nuzda bulunan ile aynı dal(branch) ada sahip yeni
    bir dal oluştuğunu göreceksiniz. Hatırlarsanız bunu yapma sebebimiz kodu remote repo'da bulunan ana kodun üzerine 
    yazmamktı
    
    Şimdi **Pull Request** denilen işlemi yapabiliriz. Bu işlem sizin yüklediğiniz değişiklikleri içeren dal(branch) ile ana
    dalı birleştirme isteğidir. Pull request, yaptığınız değişiklikleri gözden geçirmek ve ana depoya birleştirmek için 
    diğer ekip üyelerinin geri bildirimini almanızı sağlar. Bu süreçte, değişikliklerinizi açıklamalı bir şekilde 
    paylaşabilir, incelemeler ve tartışmalar yapabilirsiniz. Eğer incelemeler tamamlandı ve değişiklikler kabul edildi 
    ise, pull request **merge** (birleştirme) işlemi ile değişiklikler ana depoya entegre edilir. Bu şekilde, takımın 
    onayından geçen değişiklikler projenin güncel bir sürümünü oluşturur.
    
    Pull request oluşturarak, değişikliklerinizi yönetmek, incelemeleri yapmak ve ana depoya entegre etmek için bir 
    işbirliği üreci sağlanmış olur. Bu, projede etkili bir şekilde çalışmanızı ve takım üyeleri arasında işbirliği 
    yapmanızı kolaylaştırır.
    
    Eğer çalışmanız ile ana dalı başarılı bir şekilde birleştirmeyi başardıysanız, birleştirilmiş olan dalı, remote 
    depodan silmek, gereksiz dalların birikmesini önler. Yeni dalı remote repodan elle veya terminal aracılığıyla 
    silebilirsiniz. Bu şekilde, artık ihtiyaç duyulmayan dalların depoda bulunması engellenmiş olur.
    
    :exclamation: Bu işlemler sonrası projenin kaynak kodu güncellendi, artıl tüm kullanıcıların kendi değişikliklerini
    push etmeden önce remote repo'da gerçekleşen değişiklikleri pull etmeleri gerekmektedir.
    """)

page_3()