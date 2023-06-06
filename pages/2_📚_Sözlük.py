import streamlit as st

def page_1(term_dict):
    with st.sidebar:
        st.title("Git&GitHub terimlerinin anlamları ve kullanım alanları ile ilgli herşey:")

    st.title("Git ve GitHub Terimleri Açıklama Uygulaması :books:")
    st.write("Bu sayfada Git&GitHub denildiğinde karşınıza çıkacak farklı terimlerin ne anlama geldiğini öğrenebilirsiniz")

    term_list = [
        {"term": "Git", "description": term_dict["git"]},
        {"term": "GitHub", "description": term_dict["github"]},
        {"term": "Repository (Depo)", "description": term_dict["repo"]},
        {"term": "Commit", "description": term_dict["commit"]},
        {"term": "Branch (Dal)", "description": term_dict["branch"]},
        {"term": "Merge", "description": term_dict["merge"]},
        {"term": "Pull Request", "description": term_dict["pull_request"]},
        {"term": "Clone", "description": term_dict["clone"]},
        {"term": "Fork", "description": term_dict["fork"]},
        {"term": "Pull", "description": term_dict["pull"]}
    ]

    selected_term = st.selectbox("Bir terim seçin:", [term["term"] for term in term_list])

    for term in term_list:
        if term["term"] == selected_term:
            st.subheader(term["term"])
            st.write(term["description"])



term_dict = {
'git' : """
        **KISA AÇIKLAMA:**
        \n
        Dağıtık bir versiyon kontrol sistemi
        \n
        **DETAYLI AÇIKLAMA:**
        \n
        Git, açık kaynaklı ve dağıtık bir sürüm kontrol sistemi olarak kullanılan bir yazılımdır. Projelerin tarihçesini takip 
        etmek, değişiklikleri yönetmek ve işbirliği yapmak için kullanılır. Git, hızlı, verimli ve daldan (branch) birleştirmeye 
        (merge) kadar birçok özelliğiyle geliştiriciler arasında yaygın olarak kullanılmaktadır.
        """,
'github' : """
         **KISA AÇIKLAMA:**
        \n
        GitHub, Git adlı bir sürüm kontrol sistemini (VCS) barındıran bulut tabanlı bir hizmettir.
        \n
        **DETAYLI AÇIKLAMA:**
        \n
        GitHub, Git tabanlı projelerin barındırıldığı ve işbirliği yapıldığı bir bulut tabanlı platformdur. Geliştiriciler, 
        projelerini GitHub'a yükleyebilir, Git'i kullanarak versiyon kontrolünü yönetebilir ve diğer kullanıcılarla paylaşabilir. 
        GitHub, projelerin tarihçesini takip etmek, değişiklikleri gözden geçirmek, hataları raporlamak ve işbirliği yapmak için 
        bir dizi özellik ve araç sağlar. Ayrıca, açık kaynak projelerin topluluk tarafından katkı almasını kolaylaştıran bir 
        platformdur.
        """,
'repo' : """
         **KISA AÇIKLAMA:**
        \n
        Projedeki dosyaların ve geçmişin saklandığı yer.
        \n
        **DETAYLI AÇIKLAMA:**
        \n
        "Repo" terimi, bir Git projesinin depolama alanını veya veritabanını ifade eder. Bir repo, projenin dosyalarını, 
        tarihçesini ve yönetim özelliklerini içerir. Git repo'su, projenin geliştirilmesi, işbirliği yapılması ve sürüm 
        kontrolü için temel bir yapı taşıdır. Repo'lar, projelerin paylaşılması, değişikliklerin takip edilmesi ve geri 
        alınması için kullanılır. Projelerin popüler platformlarda veya özel sunucularda barındırılan repo'ları vardır.
        """,
'commit' : """
         **KISA AÇIKLAMA:**
        \n
        Dosya değişikliklerinin git reposuna kaydedildiği işlem.
        \n
        **DETAYLI AÇIKLAMA:**
        \n
        "Commit" (işlem), Git tabanlı bir projede yapılan değişikliklerin kalıcı olarak kaydedilmesini sağlayan bir işlemdir. 
        Bir commit, projenizin tarihçesinde bir anlık görüntüyü temsil eder ve belirli bir değişiklik paketini işaretler.
        
        Commit işlemi, projede yapılan değişikliklerin kaydedilmesiyle başlar. Önce, değişiklik yaptığınız dosyaları Git'e 
        eklemeniz gerekmektedir. Bunun için git add komutunu kullanabilirsiniz. Ardından, git commit komutunu kullanarak 
        değişiklikleri kalıcı hale getirirsiniz. Commit işlemi, bir mesaj ile birlikte yapılır. Commit mesajı, yapılan değişiklikleri 
        açıklayıcı ve anlamlı bir şekilde ifade etmelidir.
        
        Commit işlemi tamamlandığında, değişiklikler yerel projenizde kalıcı olarak kaydedilir ve Git, commit'i benzersiz bir 
        kimlikle (SHA-1 hash) tanımlar. Bu kimlik, commit'in projenin tarihçesindeki yerini belirler. Commit'ler, projenin 
        geçmişinde yapılan değişiklikleri takip etmek, geri almak veya geçmiş bir duruma dönmek için kullanılır.
        
        Commit'ler, proje yönetiminde önemli bir rol oynar. Her commit, yapılan değişikliklerin izlenebilirliğini sağlar ve 
        projenin tutarlılığını korur. Düzgün bir commit akışı, proje ekibinin işbirliği yapmasını kolaylaştırır ve projenin 
        gelişiminin izlenmesini sağlar. Ayrıca, anlamlı ve açıklayıcı commit mesajları yazmak, projenin geçmişini daha iyi 
        anlamamızı ve projede yapılan değişikliklerin amacını ve etkisini hızlıca anlamamızı sağlar.
        """,
'branch' : """
         **KISA AÇIKLAMA:**
        \n
        Projedeki ana kaynaktan türetilen ayrı bir çalışma alanı.
        \n
        **DETAYLI AÇIKLAMA:**
        \n
        "Branch" (dal), Git tabanlı bir proje yönetiminde kullanılan ve projenin farklı çalışma alanlarını, özelliklerini veya 
        sürümlerini izlemek ve yönetmek için kullanılan bir kavramdır. Bir branch, projenin mevcut durumundan bağımsız olarak 
        yeni bir çalışma alanı oluşturur.
        
        Bir branch oluşturmak, mevcut projenin ana dalından (genellikle "master" veya "main" olarak adlandırılır) ayrılan ve 
        kendi değişikliklerinizi izleyebileceğiniz bir dal yaratmanızı sağlar. Her branch, proje içerisindeki dosyaların kopyasını 
        tutar ve üzerinde yapılan değişiklikler, sadece o dalı etkiler. Branch'ler, aşağıdaki senaryolarda kullanılabilir:
        
        - Feature Branches: Yeni bir özelliği geliştirirken veya mevcut bir özelliği değiştirirken, ana dalın dışında bir branch 
        oluşturabilirsiniz. Bu, ana dala etki etmeden özellik üzerinde çalışmanıza olanak tanır. Özelliği tamamladıktan sonra, 
        branch'i ana dal ile birleştirebilirsiniz.
        - Release Branches: Bir projenin belirli bir sürümünü hazırlarken, mevcut durumu korumak ve son düzeltmeleri eklemek için
        bir release branch oluşturabilirsiniz. Bu, projenin mevcut sürümündeki hataları düzeltmek veya son dakika değişiklikleri 
        yapmak için kullanışlıdır.
        - Hotfix Branches: Canlı bir projede acil bir hata veya güvenlik açığı bulduğunuzda, ana dalı bozmadan hızlı bir şekilde
        düzeltme yapmak için bir hotfix branch oluşturabilirsiniz. Bu dal, ana dalın mevcut sürümünden ayrılır, hızlı bir düzeltme
        yapmanıza ve ardından ana dal ve diğer branch'lerle birleştirme yapmanıza olanak sağlar.
        
        Branch'ler, projede aynı anda farklı özellikler veya değişiklikler üzerinde çalışmanızı sağlar. Her branch, bağımsız olarak 
        yönetilebilir, değişiklikleri izleyebilir, test edebilir ve gerektiğinde diğer branch'lerle birleştirilebilir. Bu, paralel
        çalışmayı kolaylaştırır, çatışmaları azaltır ve projenin daha iyi organize edilmesine yardımcı olur.
        """,
'merge' : """
         **KISA AÇIKLAMA:**
        \n
        Farklı dallardaki değişikliklerin birleştirildiği işlem.
        \n
        **DETAYLI AÇIKLAMA:**
        \n
        "Remote merge" terimi, uzak Git depolarında (remote repositories) yapılan birleştirme (merge) işlemini ifade eder. Uzak 
        merge işlemi, farklı kullanıcıların veya ekiplerin çalışmalarını birleştirmek için uzak depoları kullanır. Uzak merge işlemi 
        genellikle aşağıdaki adımları içerir:
        
        - İlk olarak, yerel projenizde çalışmak üzere uzak depoyu (remote repository) klonlamış olmanız gerekir.
        - Uzak depoyu klonladıktan sonra, projenin başka bir katılımcısı veya ekibi uzak depoda (remote repository) değişiklikler 
        yapar ve bunları uzak depoya (remote repository) itebilir.
        - Uzak depoda (remote repository) yapılan değişiklikleri yerel projenize entegre etmek için git pull komutunu kullanabilirsiniz. 
        Bu komut, yerel projenizi uzak depoyla senkronize eder ve uzak depodaki değişiklikleri yerel projenize çeker.
        - Eğer uzak depoda (remote repository) yapılan değişiklikler yerel projenizde çakışmalara (conflicts) neden olursa, bu 
        çakışmaları düzeltmeniz gerekebilir. Çakışmaları çözmek için Git, değişikliklerinizi ve diğer katılımcıların değişikliklerini 
        birleştirme (merge) işlemiyle bir araya getirir.
        - Çakışmaları çözdükten sonra, değişiklikleri commit'leyebilir ve gerekli durumlarda push işlemiyle uzak depoya (remote 
        repository) gönderebilirsiniz.
        
        Uzak merge işlemi, projenin farklı katılımcıları veya ekipleri arasında çalışmaları birleştirme ve projenin güncel halini 
        tutma amacıyla kullanılır. Uzak depodaki (remote repository) değişiklikleri yerel projenize entegre etmek, işbirliğini kolaylaştırır 
        ve proje ekibinin güncel çalışma durumunu sağlar.
        """,
'pull_request' : """
         **KISA AÇIKLAMA:**
        \n
        Değişikliklerin ana dala birleştirilmesi için yapılan bir istek.
        \n
        **DETAYLI AÇIKLAMA:**
        \n
        "Pull request" (çekme isteği), Git tabanlı bir proje yönetiminde kullanılan bir işlemdir. Bir pull request, değişikliklerin 
        önerildiği ve incelenmesi için projenin sahiplerine gönderildiği bir istektir. Bir pull request oluşturmak için aşağıdaki adımları izleyebilirsiniz:
        
        - Proje deposunu (repository) fork ederek kendi hesabınıza kopyalayın.
        - Kopyalanan projeyi yerel makinenize klonlayın.
        - Yerel projenizde yeni bir dal (branch) oluşturun ve değişikliklerinizi bu dalda yapın.
        - Yapılan değişiklikleri commit'leyin ve yerel projenizin dalına (branch) gönderin.
        - GitHub veya Git tabanlı platformdaki kendi hesabınıza giriş yapın.
        - Fork edilen projenin deposuna gidin ve "New Pull Request" veya "Pull Request Oluştur" düğmesine tıklayın.
        - Karşınıza gelen sayfada, hangi değişiklikleri hangi dallardan (branch) projenin ana dalına (main branch) entegre etmek istediğinizi belirtin.
        - Pull request'i oluşturmak için gerekli bilgileri (başlık, açıklama vb.) girin.
        - Oluşturulan pull request, projenin sahiplerine iletilir ve incelenir.
        - Proje sahipleri pull request'i gözden geçirir, değişiklikleri değerlendirir ve projeye entegre etmek veya geri bildirim sağlamak için gereken adımları atar.
        
        Pull request, bir projeye katkıda bulunmanın ve değişiklikleri projenin ana dalına entegre etmenin yaygın bir yoludur. 
        Diğer projenin sahipleri, pull request'i inceleyerek değişiklikleri gözden geçirebilir, tartışabilir ve projeye katkı 
        sağlayabilir. Pull request, işbirliğini kolaylaştırır, kod incelemeleri ve proje kalitesi için bir mekanizma sağlar ve 
        değişikliklerin kontrollü bir şekilde projeye entegre edilmesini sağlar.
        """,
'clone' : """
         **KISA AÇIKLAMA:**
        \n
        Uzak repo kaynağının yerel makineye kopyalanması.
        \n
        **DETAYLI AÇIKLAMA:**
        \n
        "Clone" komutu, Git'in bir komutudur ve bir uzak Git deposundaki projenin tam bir kopyasını yerel makinenize indirmenizi 
        sağlar. Klonlama işlemi, projenin tüm dosyalarını, geçmişini ve yapılandırmasını içerir.
        
        Klonlama işlemi, projeyi yerel makinenizde kullanmak ve düzenlemek için gereklidir. Bu şekilde, projenin dosyalarına 
        erişebilir, değişiklikler yapabilir ve bu değişiklikleri takip edebilirsiniz. Klonlama, aynı zamanda projenin geçmişini 
        de indirir, böylece projenin her bir değişikliğini geriye dönük olarak gözden geçirebilir ve geçmiş sürümlere erişebilirsiniz.
        
        Klonlama işlemi için, projenin Git deposunun URL'sini ve klonlama hedefini belirtmeniz gerekir. URL, projenin uzak depoya 
        erişim adresidir ve genellikle "https://" veya "git://" ile başlar. Klonlama hedefi, projenin yerel makinenizde oluşturulacak 
        klasörün adını temsil eder. Bu adımları takip ederek, Git komutunu kullanarak projenin tam bir kopyasını indirebilir ve yerel 
        makinenizde çalışmaya başlayabilirsiniz.
        
        Klonlama işlemi, dağıtık bir versiyon kontrol sistemi olan Git'in en temel ve önemli özelliklerinden biridir. Klonlanan 
        projeyi yerelde düzenleyebilir, yeni özellikler ekleyebilir, hataları düzeltebilir ve değişiklikleri geriye dönük olarak 
        yönetebilirsiniz. Bu sayede, projeye katkıda bulunabilir veya kendi bağımsız projenizi geliştirebilirsiniz.
        """,
'fork' : """
         **KISA AÇIKLAMA:**
        \n
        Bir projenin tam bir kopyasını kullanıcının GitHub hesabına taşıma işlemi.
        \n
        **DETAYLI AÇIKLAMA:**
        \n
        "Fork" terimi, açık kaynaklı bir projenin kopyasını almak anlamına gelir. Genellikle başka bir projenin geliştirilmesine 
        veya katkıda bulunulmasına olanak sağlamak için kullanılır.
        
        Bir projeyi "fork" ettiğinizde, projenin tam bir kopyası sizin GitHub (veya başka bir Git tabanlı platformda) hesabınıza 
        taşınır. Bu noktadan itibaren, projeyi bağımsız bir şekilde yönetebilirsiniz. Fork işlemi, orijinal projenin gelişimine 
        etki etmez ve değişiklikleriniz orijinal projeye yansıtılmaz. Fork ettiğiniz projenin tam kontrolü sizdedir ve bu projede 
        dilediğiniz değişiklikleri yapabilirsiniz.
        
        Fork işlemi, açık kaynaklı projelerde katkıda bulunmanın yaygın bir yoludur. Fork ettiğiniz projeyi kendi hesabınıza 
        taşıyarak projeyi bağımsız olarak geliştirebilir, hataları düzeltebilir, yeni özellikler ekleyebilir veya projenin 
        orijinaline geri dönerek değişikliklerinizi paylaşabilirsiniz. Fork edilen projede yaptığınız değişiklikleri, "pull request" 
        (çekme isteği) yoluyla orijinal projenin sahiplerine gönderebilir ve bu şekilde katkı sağlayabilirsiniz.
        """,
'pull' : """
         **KISA AÇIKLAMA:**
        \n
        Uzak repo kaynağını yerel makineye güncelleme işlemi.
        \n
        **DETAYLI AÇIKLAMA:**
        \n
        "Pull" işlemi, Git'in bir komutudur ve yerel projenizi güncellemek için uzak Git deposundan en son değişiklikleri almanızı 
        sağlar. Bu işlem, projenizin diğer katılımcılarla senkronize olmasını sağlar ve projenin en güncel halini yerel makinenize 
        getirir. Pull komutu kullanılarak, uzak depoda yapılan değişikliklerin yerel projenize entegre edilmesi sağlanır, böylece 
        projenin en son sürümüne erişebilir ve diğer katılımcılarla yapılan değişiklikleri paylaşabilirsiniz.
        """
}

page_1(term_dict)