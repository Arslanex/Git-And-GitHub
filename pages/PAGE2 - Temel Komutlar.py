import streamlit as st
from Beginner_Commands import *

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


page_2()