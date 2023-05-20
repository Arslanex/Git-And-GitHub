import streamlit as st

def page_2():
    st.title("Temel Git&GitHub komutları :paperclip:")
    st.write("Bu sayfada temel seviye Git&GitHub kullanmak için gerekli komutları ve kullanım şekillerini öğrenebilirsiniz.")

    st.subheader("Kendinizi Tanıtın")
    with st.expander("See explanation"):
        st.markdown(p2_desc)
        st.text(p2_example1)
        st.code(code_config, language="bash")
        st.text(p2_example2)
        st.code(code_validate, language="bash")

    st.subheader("git init")
    with st.expander("See explanation"):
        st.markdown(p3_desc)
        st.text(p3_example1)
        st.code(code_cd, language='bash')
        st.text(p3_example2)
        st.code(code_init, language='bash')
        st.markdown(p3_outro)

    st.subheader("git clone")
    with st.expander("See explanation"):
        st.markdown(p4_desc)
        st.code(code_clone, language='bash')

    st.subheader("git add")
    with st.expander("See explanation"):
        st.markdown(p5_desc)
        st.text(p5_example1)
        st.code(code_add, language='bash')
        st.text(p5_example2)
        st.code(code_add_all)
        st.markdown(p5_outro)

    st.subheader("git commit")
    with st.expander("See explanation"):
        st.markdown(p6_desc)
        st.code(code_commit_m, language='bash')
        st.markdown(p6_t2)
        st.code(code_commit_a, language='bash')
        st.markdown(p6_outro)

    st.subheader("git status")
    with st.expander("See explanation"):
        st.markdown(p7_desc)
        st.code(code_status, language='bash')
        st.markdown(p7_outro)

    st.subheader("git branch (Dallar Arası İşlemler)")
    with st.expander("See explanation"):
        st.markdown(p8_desc)
        st.write(p8_t1)
        st.code(code_checkout_b, language='bash')
        st.write(p8_t2)
        st.code(code_checkout, language='bash')
        st.write(p8_t3)
        st.code(code_branch, language='bash')
        st.write(p8_t4)
        st.code(code_checkout_d, language='bash')

    st.subheader("remote repo (GitHub)")
    with st.expander("See explanation"):
        st.markdown(p9_t1)
        st.code(code_add_ip, language='bash')
        st.markdown(p9_t2)
        st.code(code_add_link, language='bash')
        st.markdown(p9_t3)
        st.code(code_add_remote, language='bash')
        st.markdown(p9_outro)

    st.subheader("git push")
    with st.expander("See explanation"):
        st.markdown(p10_t1)
        st.code(code_push_branch, language='bash')
        st.markdown(p10_t2)
        st.code(code_push_all, language='bash')
        st.markdown(p10_t3)
        st.code(code_push_delete, language='bash')

    st.subheader("git pull / git fetch")
    with st.expander("See explanation"):
        st.markdown(p11_t1)
        st.code(code_pull, language='bash')
        st.markdown(p11_t2)
        st.code(code_fetch, language='bash')
        st.markdown(p11_t3)
        st.code(code_merge, language='bash')
        st.markdown(p11_t4)
        st.code(code_rebase, language='bash')




# Part 2
p2_desc = """
    Git kullanmaya başlamadan önce, kendinizi tanıtmanız gerekiyor. Bunun nedeni, kimin hangi değişiklikleri yaptığını 
    takip etmek ve birden fazla kişiyle çalıştığınızda karışıklığı önlemek içindir. Bu adımı atlamak, projenin yönetiminde 
    zorluklara neden olabilir.

    Kendinizi tanıtmak için, Git'in terminalinde adınızı ve email adresinizi ayarlayabilirsiniz. Aşağıdaki adımları takip edin:
    """
p2_example1 = "Adınızı ve email adresinizi ayarlayın:"
code_config = """
                git config --global user.name "Adınız Soyadınız"
                git config --global user.email "email@example.com"
             """
p2_example2 = "İşlemi doğrulayın:"
code_validate = """
                git config --global user.name
                git config --global user.email
             """

# Part 3
p3_desc = """
    Git kullanmaya başlamak için ilk adım, yerel bir Git deposu oluşturmaktır. Bu işlem, projenizi Git ile takip etmek ve 
    değişiklikleri yönetmek için gerekli olan temel yapıyı oluşturur. git init komutu, bir dizini boş bir Git deposuna 
    dönüştürmek için kullanılır. İşte git init komutunu nasıl kullanacağınızın adımları:
        """
p3_example1 = "Git'in terminalini açın ve projenizi oluşturmak istediğiniz dizine gidin:"
code_cd = "cd proje-dizini/"
p3_example2 = "Yeni bir Git deposu oluşturmak için aşağıdaki komutu girin:"
code_init = "git init"
p3_outro = """
git init komutunu çalıştırdığınızda, proje dizininizde gizli bir .git klasörü oluşturulur. Bu klasör, Git deposunun tüm verilerini ve geçmişini içerir.
"""

# Part 4
p4_desc = """
        "check out", bir depodan bir kopya almayı veya erişmeyi ifade eden bir terimdir. Bu kopya üzerinde değişiklik 
        yapabilir, yeni özellikler ekleyebilir veya hataları düzeltebilirsiniz.

        Git kullanırken başka bir deposu üzerinde çalışmak istediğinizde, git clone komutunu kullanarak o depodan yerel 
        bir kopya oluşturabilirsiniz. Bu, mevcut bir depoyu klonlayarak, depodaki tüm dosyaları ve geçmişi yerel bir dizine 
        kopyalamanızı sağlar. git clone komutu, hem yerel depoları hem de uzak sunuculardaki depoları klonlamak için kullanılabilir. 
"""
code_clone = "git clone /dizin/yolu/depoyu"

# Part 5
p5_desc = """
Git kullanırken, değişiklik yaptığınız dosyaları takip etmek ve bir sonraki commit işlemi için hazırlamak için git add 
komutunu kullanabilirsiniz. Bu komut, belirli dosyaları veya tüm dosyaları "staging" olarak adlandırılan bir alana ekler. 
İşte git add komutunu kullanmanızın adımları:
"""
p5_example1 = "Bir dosyayı 'staging' alanına eklemek için:"
code_add = "git add dosya-adi"
p5_example2 = "veya tüm dosyaları eklemek için:"
code_add_all = "git add *"
p5_outro = "Bu komutlar, belirtilen dosyayı veya tüm dosyaları 'staging' alana ekler. 'Staging' alanı, bir sonraki commit işleminde yer alacak değişiklikleri belirtir."

# Part 6
p6_desc = """
Git kullanırken, yapılan değişiklikleri kaydetmek ve bir sonraki aşamaya geçmek için git commit komutunu kullanabilirsiniz. 
Bu komut, "staging" alandaki dosyaları kaydederek bir "commit" oluşturur. İşte git commit komutunu kullanmanızın adımları:
"""
code_commit_m = 'git commit -m "Commit mesajı"'
p6_t2 = """
Eğer git add komutuyla eklediğiniz dosyalarınız varsa ve ayrıca o zamandan beri değiştirdiğiniz dosyalarınız varsa, bu 
dosyaları commit etmek için aşağıdaki adımları izleyebilirsiniz:
"""
code_commit_a = 'git commit -a -m "Commit mesajı"'
p6_outro = """
- -a parametresi, hem git add ile eklediğiniz dosyaları hem de değiştirdiğiniz dosyaları commit etmek için kullanılır.
- -m parametresi, commit mesajını tanımlamanızı sağlar. Commit mesajı, yapılan değişiklikleri açıklayan ve anlaşılır bir şekilde belirten bir ifadedir. Mesajı kısa ve öz tutmaya özen gösterin.
"""

# Part 7
p7_desc = """
it kullanırken, mevcut proje dizininde yapılan değişiklikleri ve projenin durumunu kontrol etmek için git status komutunu 
kullanabilirsiniz. Bu komut, Git deposunun mevcut durumunu gösterir ve değişikliklerin hangi dosyalarda olduğunu, hangi 
dosyaların "staging" alanında olduğunu ve hangi dosyaların commit edilmesi gerektiğini belirtir. İşte git status komutunu kullanmanızın adımları:
"""
code_status = "git status"
p7_outro = """
Bu komut, Git deposunun durumunu gösteren bir çıktı üretecektir. Çıktı, aşağıdaki gibi bilgiler içerebilir:

- Hangi dosyaların değiştirildiği veya yeni dosyaların eklenip eklenmediği
- Hangi dosyaların "staging" alanda olduğu (yeşil renkle gösterilir)
- Hangi dosyaların henüz "staging" alana eklenmediği (kırmızı renkle gösterilir)
- Henüz commit edilmemiş değişikliklerin özeti
"""

# Part 8
p8_desc = """
Git'te branch, farklı işlemleri birbirinden bağımsız olarak gerçekleştirmenizi sağlayan bir paralel 
evren olarak düşünülebilir. Her branch, farklı bir işlevi veya özelliği temsil eder ve her birinde 
yapılan değişiklikler yalnızca ilgili branch'i etkiler. Bu sayede, birden fazla özelliğin eş zamanlı 
olarak geliştirilmesi ve yönetilmesi mümkün olur.
"""
p8_t1 = "Yeni bir branch oluşturmak ve ona geçmek için aşağıdaki adımları izleyebilirsiniz:"
code_checkout_b = "git checkout -b <branchname>"
p8_t2 = "Bir branch'ten hedeflediğiniz branch'e geçiş yapmanızı sağlayabilirsiniz :"
code_checkout = "git checkout <branchname>"
p8_t3 = "Var olan tüm branch'leri listeler :"
code_branch = "git branch"
p8_t4 = "Belirtilen branch'i siler :"
code_checkout_d = "git branch -d <branchname>"

# Part 9
p9_t1 = "Uzak sunucuyu eklemek için git remote add origin <sunucu> komutunu kullanın:"
code_add_ip = "git remote add origin sunucu-adresi"
p9_t2 = """
Bu komut, yerel depoyu uzak bir sunucuya bağlar. <sunucu> parametresi, bağlanmak istediğiniz sunucunun adresini temsil eder. Örneğin, 
GitHub'da oluşturduğunuz bir uzak depoya bağlanmak için aşağıdaki komutu kullanabilirsiniz:
"""
code_add_link = "git remote add origin https://github.com/kullanici-adi/proje-repo.git"
p9_t3 = "Şu anda yapılandırılmış olan tüm uzak depoları listelemek için git remote -v komutunu kullanabilirsiniz:"
code_add_remote = "git remote -v"
p9_outro = """
Eğer bir projeyi zaten git clone komutuyla klonladıysanız, projenin otomatik olarak bir uzak sunucu bağlantısı zaten mevcut 
olacaktır. Bu durumda, ayrıca ' git remote add origin <sunucu> ' komutunu kullanmanıza gerek yoktur.
"""

# Part 10
p10_t1 = "Bu komut, belirttiğiniz dalı (<branchadı>) uzak depoya (origin) gönderir :"
code_push_branch = "git push origin dal-adı"
p10_t2 = "Bu komut, tüm dalları uzak depoya (origin) gönderir."
code_push_all = "git push --all origin"
p10_t3 = "Belirtilen dalı (<branchadı>) uzak depodan (origin) siler :"
code_push_delete = "git push origin --delete dal-adı"

# Part 11
p11_t1 = " uzak sunucudan (uzak depo) en son değişiklikleri çeker ve yerel çalışma dizininizdeki mevcut dalı günceller :"
code_pull = "git pull"
p11_t2 = " Bu komut, uzak depodan (uzak sunucudan) en son değişiklikleri çeker, ancak yerel çalışma dizinindeki dosyaları güncellemez veya değiştirmez. "
code_fetch = "git fetch"
p11_t3 = " belirtilen dalı (<branchadı>) mevcut aktif dalınıza birleştirir. "
code_merge = "git merge dal-adı"
p11_t4 = """
 komutu, mevcut bir dalı başka bir dalın son değişiklikleriyle yeniden düzenlemek için kullanılır.
  Yani, mevcut dalınızın tarih sırasını değiştirmek ve başka bir dalın sonundaki değişiklikleri 
  mevcut dalınıza eklemek için git rebase komutunu kullanabilirsiniz.
"""
code_rebase = "git rebase hedef-dal"

page_2()