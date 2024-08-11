import streamlit as st
from collections import OrderedDict

from tabs import intro, selection, viz, models, interpretability, conclusion

# Define the custom CSS to change the background color
st.markdown(
    """
    <style>
    .stApp {
        background-color: #F0F0F0; 
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Order the tabs, ensuring intro is first
TABS = OrderedDict(
    [
        (intro.sidebar_name, intro),
        (selection.sidebar_name, selection),
        (viz.sidebar_name, viz),
        (models.sidebar_name, models),
        (interpretability.sidebar_name, interpretability),
        (conclusion.sidebar_name, conclusion),
    ]
)

def run():
    st.sidebar.image(
        "credit approval.jpg",
        width=200,
    )
    
    # Set the first tab to be 'intro'
    tab_name = st.sidebar.radio("Navigation", list(TABS.keys()), index=0)
    st.sidebar.markdown("---")

    tab = TABS[tab_name]
    tab.run()

if __name__ == '__main__':
    run()
