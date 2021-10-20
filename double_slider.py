#Frame 1
import streamlit as st

st.title("Streamlit Double Sliders")

#frame 2
st.subheader("Slider")
slider_range = st.slider("Double ended slider", value=[100,400])
#
#frame 3
st.info("Our slider range has type: %s" %type(slider_range))
#
#frame 4
st.write("Slider range:", slider_range, slider_range[0], slider_range[1])
#
#Frame 5
st.subheader("Select Slider")
rainbow = ['red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'violet']
start_clr, end_clr = st.select_slider("Select a range of colors from the rainbow",
    options=rainbow, value=('orange','indigo'))
#
# Frame 5
st.info("Our colours have types: %s" %type(start_clr))
st.write('You chose:', start_clr, "to", end_clr)
