import streamlit as st
from Text.Beginner_Commands import *
st.set_page_config(
    page_title="Beginner"
)

st.title("Yeni başlayanlar için bilinmesi gerekenler :")

# Tanıtım
st.header("Nedir bu Git&GitHub ?")
st.markdown(
    """
    **:orange[Git]**, bir sürüm kontrol sistemi olarak bilinen bir yazılımdır. Projelerinizde yapılan değişiklikleri takip etmenize, 
    geçmiş versiyonları geri getirmenize ve paralel çalışma yapmanıza olanak sağlar. Bu, bir projenin farklı sürümlerini 
    ve değişikliklerini takip etmenizi sağlar. Git'in merkezi olmayan bir yapıya sahip olması, bağımsız çalışmayı ve 
    paralel geliştirme yapmayı kolaylaştırır.

    **:orange[GitHub]** ise, Git tabanlı bir web platformdur. Projelerinizi Git deposunda barındırmanıza ve işbirliği yapmanıza 
    olanak sağlar. GitHub, birçok işlevi bir araya getirerek projelerinizi paylaşmanızı, diğer geliştiricilerle etkileşime 
    geçmenizi ve açık kaynak projelerine katkıda bulunmanızı kolaylaştırır. Bir projenin kaynak kodunu GitHub'da barındırıyorsanız, 
    diğer insanlar kolayca projenize katkıda bulunabilir veya geribildirim sağlayabilir.

    Kısacası, Git bir sürüm kontrol sistemi iken, GitHub ise Git tabanlı bir işbirliği platformudur. Git, yerel bilgisayarınızda 
    çalışırken, GitHub projelerinizi bulut tabanlı bir ortamda barındırır ve işbirliği yapmanıza olanak tanır. Git, projelerinizin 
    geçmişini ve değişikliklerini takip ederken, GitHub projelerinizi paylaşmanızı, işbirliği yapmanızı ve toplulukla etkileşime geçmenizi sağlar.
    """
)

st.header("Git'e Başlarken")
st.markdown(p2_desc)
st.text(p2_example1)
st.code(code_config, language="bash")
st.text(p2_example2)
st.code(code_validate, language="bash")

st.header("Local bir git reposu oluşturun")
st.markdown(p3_desc)
st.text(p3_example1)
st.code(code_cd, language='bash')
st.text(p3_example2)
st.code(code_init, language='bash')
st.markdown(p3_outro)

st.header("Bir Repo Check Out Edin")
st.markdown(p4_desc)
st.code(code_clone, language='bash')

st.header("Çalışma Dosyalarınız Ekleyin")
st.markdown(p5_desc)
st.text(p5_example1)
st.code(code_add, language='bash')
st.text(p5_example2)
st.code(code_add_all)
st.markdown(p5_outro)

st.header("Commit İşlemi")
st.markdown(p6_desc)
st.code(code_commit_m, language='bash')
st.markdown(p6_t2)
st.code(code_commit_a, language='bash')
st.markdown(p6_outro)

st.header("Yerel Reponuzu Kontrol Edin")
st.markdown(p7_desc)
st.code(code_status, language='bash')
st.markdown(p7_outro)

st.title("Branch İşlemleri")
st.markdown(p8_desc)
st.write(p8_t1)
st.code(code_checkout_b, language='bash')
st.write(p8_t2)
st.code(code_checkout, language='bash')
st.write(p8_t3)
st.code(code_branch, language='bash')
st.write(p8_t4)
st.code(code_checkout_d, language='bash')

st.title("Remote bir Repoya Bağlan :")
st.markdown(p9_t1)
st.code(code_add_ip ,language='bash')
st.markdown(p9_t2)
st.code(code_add_link ,language='bash')
st.markdown(p9_t3)
st.code(code_add_remote ,language='bash')
st.markdown(p9_outro)

st.title("Remote Repoya Gönderma Yapın :")
st.markdown(p10_t1)
st.code(code_push_branch,language='bash')
st.markdown(p10_t2)
st.code(code_push_all,language='bash')
st.markdown(p10_t3)
st.code(code_push_delete,language='bash')

st.title("Uzak Depodan Güncellemeleri Almak")
st.markdown(p11_t1)
st.code(code_pull, language='bash')
st.markdown(p11_t2)
st.code(code_fetch, language='bash')
st.markdown(p11_t3)
st.code(code_merge, language='bash')
st.markdown(p11_t4)
st.code(code_rebase, language='bash')
