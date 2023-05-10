import streamlit as st

st.title("Bir Takım İle Git&GitHub Kullanımı")
st.markdown("""
Bu sayfada, takım olarak çalışırken Git ve GitHub teknolojilerini nasıl kullanabileceğinizi ve bu konuda yapmanız gereken 
hazırlıkları anlatıyoruz. Buradaki içerikler başlangıç seviyesinde olanlar için tasarlanmıştır. Ancak ilerleyen sayfalarda, 
daha gelişmiş yöntemlere de yer vereceğiz.

Bu sayfayı okumadan önce, önceki sayfalarda bulunan tanımları ve örnekleri gözden geçirmenizi ve takıldığınız yerlerde 
geriye dönüp bakmanızı öneririm. Bu şekilde, bu sayfadaki içeriği daha iyi anlayabilir ve daha verimli bir şekilde takip 
edebilirsiniz. Hazırsanız hızlıca başlayalım.
""")

st.header("1.ADIM: Sanal Dünyada Ortak Bir Çalışma Alanı Oluşturun")
st.markdown("""
Projeyi yönetmek ve işbirliği yapmak için Git hizmeti sağlayıcısında bir depo oluşturmak önemlidir. Bu depo, tüm ekibin 
projeye erişebileceği ve üzerinde çalışabileceği merkezi bir konum sağlar. İşte adımlar:

- Git hizmeti sağlayıcısı seçimi: Öncelikle, Git hizmeti sağlayıcısı olarak GitHub, GitLab veya Bitbucket gibi popüler 
platformlardan birini seçmeniz gerekir. Bu platformlar, projelerinizi yönetmek ve takımınızla işbirliği yapmak için gerekli 
araçları sağlar.

- Hesap oluşturma: Seçtiğiniz Git hizmeti sağlayıcısının web sitesine giderek bir hesap oluşturmanız gerekmektedir. Genellikle, 
hesap oluşturmak ücretsizdir, ancak bazı ek özellikler için ücretli planlara geçiş yapabilirsiniz.

- Yeni bir depo oluşturma: Hesabınızı oluşturduktan sonra, projenizin yer alacağı yeni bir depo oluşturmanız gerekecektir. 
Genellikle, "New Repository" veya benzeri bir düğme ile yeni depo oluşturma seçeneği bulunur. Depo oluşturma işlemi sırasında, 
depo adını, açıklamasını ve gizlilik ayarlarını belirlemeniz istenecektir.

- Depo ayarları: Depo oluşturulduktan sonra, bazı ayarları düzenlemeniz gerekebilir. Örneğin, ekip üyelerini depoya davet 
etmek, geliştirme sürecini kolaylaştıracak ek özellikleri etkinleştirmek veya depo izinlerini ayarlamak gibi adımları takip 
etmeniz gerekebilir.

- İlk kodunuzu gönderme: Depo oluşturulduktan sonra, projenizin ilk kodunu göndermek için Git istemcisini kullanabilirsiniz. 
Git istemcisi, projenizin yerel bir kopyasını oluşturmanızı ve ardından değişiklikleri depoya göndermenizi sağlar. Bu sayede, 
takımınızla kod paylaşabilir ve projenin güncel bir sürümünü depoda tutabilirsiniz.

Bu adımları takip ederek, Git hizmeti sağlayıcısında bir depo oluşturabilir ve takımınızla işbirliği yapabilirsiniz. Bu
depo, projenizin merkezi bir noktası haline gelecek ve tüm ekibin güncellemeleri takip etmesine ve üzerinde çalışmasına 
olanak sağlayacaktır.
""")

st.header("2.ADIM: Oluşturduğunuz Sanal Deponun Kopyasını Yerel Cihazınıza Klonlayın")
st.markdown("""
Online depoyu yerel bilgisayarınıza klonlamak, projenin mevcut halini indirerek yerel çalışma alanınıza getirmenizi sağlar. 
Böylece projeyi yerel olarak düzenleyebilir ve değişiklikler yapabilirsiniz.
""")
st.code("git clone <remote-repo-URL>", language='bash')
st.markdown("""
Unutmayın, projenin yerel kopyasında yaptığınız değişiklikler online depoyu etkilemez. Değişiklikleri online depoya göndermek 
için Git komutlarını kullanmanız gerekmektedir.
""")

st.header("3.ADIM: Güncellemeleri Kontrol Edin")
st.markdown("""
`git pull` komutunu kullanarak diğer ekip üyelerinin yaptığı güncellemeleri alabilir ve yerel çalışma alanınızı güncel tutabilirsiniz. 
Bu komut, uzaktaki depodaki en son değişiklikleri indirerek yerel kopyanıza entegre eder.

Ayrıca, `git fetch` komutunu da kullanabilirsiniz. `git fetch`, uzaktaki depodaki güncellemeleri indirir, ancak yerel çalışma alanınızı 
otomatik olarak güncellemez. Yani, `git fetch` ile indirilen güncellemeleri, `git merge` veya `git rebase` gibi komutlarla yerel kopyanıza 
entegre etmeniz gerekir.

git pull komutu, `git fetch` ve `git merge` işlemlerini birleştirir. Yani, `git pull` komutunu kullanarak hem güncellemeleri 
indirebilir hem de otomatik olarak yerel çalışma alanınızı güncelleyebilirsiniz.
""")

st.header("4.ADIM: Çalışmalarınız için Kendinize Branch Oluşturun")
st.markdown("""
kendi adınıza bir dal oluşturarak değişikliklerinizi bu dal üzerinde gerçekleştirebilirsiniz. Bu şekilde, diğer ekip 
üyelerinin çalışmalarından etkilenmeden bağımsız bir şekilde çalışabilirsiniz. Ardından, değişikliklerinizi bu dal üzerinde 
kaydedebilir ve gerekli olduğunda ana dal (master) veya diğer dallarla birleştirebilirsiniz.
""")
st.code("git branch <branch-adı>", language='bash')
st.code("git checkout <branch-adı>", language='bash')

st.header("5.ADIM: Yaptığınız Değişiklikleri Kayıt Edin")
st.markdown("""
Yaptığınız değişiklikleri `git add` komutuyla ekledikten ve `git commit` komutuyla kaydettikten sonra, değişiklikler yerel 
olarak kaydedilir. Ancak, bu değişiklikler henüz online depoya gönderilmemiş olur. Bunları online depoya göndermek için 
`git push` komutunu kullanmanız gerekecektir.
""")
st.code("git add <dosya-adı>", language='bash')
st.code("git commit -m 'Değişiklik açıklaması'", language='bash')

st.header("6.ADIM: Yaptığınız Değişiklikleri Ana Repoya Gönderin")
st.markdown("""
Git push komutu, yaptığınız değişiklikleri uzaktaki depoya göndermek için kullanılır. Bu sayede, projedeki diğer ekip 
üyeleriyle işbirliği yapabilir ve çalışmalarınızı senkronize edebilirsiniz.
""")
st.code("git push origin <branch-adı>", language='bash')

st.header("7.ADIM Pull Request ve Merge")
st.markdown("""
Yaptığınız git push komutu, değişikliklerinizi uzaktaki depoya gönderir ve yeni bir dal oluşturur. Bu yeni dal, 
değişikliklerinizi ana depo ile birleştirmek için diğer ekip üyelerinin incelemesine sunmanızı sağlar.

Daha sonra, uzaktaki depoda oluşturduğunuz yeni dal üzerinden bir pull request (çekme isteği) oluşturmanız gerekir. Pull 
request, yaptığınız değişiklikleri gözden geçirmek ve ana depoya birleştirmek için diğer ekip üyelerinin geri bildirimini 
almanızı sağlar. Bu süreçte, değişikliklerinizi açıklamalı bir şekilde paylaşabilir, incelemeler ve tartışmalar yapabilirsiniz.

Diğer ekip üyeleri, pull request'i inceleyebilir, değişiklikleri karşılaştırabilir ve yorumlarını ekleyebilir. Eğer incelemeler 
tamamlandı ve değişiklikler kabul edildi ise, pull request merge (birleştirme) işlemi ile değişiklikler ana depoya entegre edilir. 
Bu şekilde, takımın onayından geçen değişiklikler projenin güncel bir sürümünü oluşturur.

Pull request oluşturarak, değişikliklerinizi yönetmek, incelemeleri yapmak ve ana depoya entegre etmek için bir işbirliği 
süreci sağlanmış olur. Bu, projede etkili bir şekilde çalışmanızı ve takım üyeleri arasında işbirliği yapmanızı kolaylaştırır.
""")

st.header("8. Dalı silin")
st.markdown("""
Birleştirilmiş olan dalı, remote depodan silmek, gereksiz dalların birikmesini önler. Yeni dalı remote repodan elle veya 
terminal aracılığıyla silebilirsiniz. Bu şekilde, artık ihtiyaç duyulmayan dalların depoda bulunması engellenmiş olur
""")
st.code("git push origin --delete <dal-adı>", language='bash')
