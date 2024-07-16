import streamlit as st
st.title('Display text')


st.text('Fixed width text')
st.markdown('_MARKDOWN_')
st.caption('Balloons. Hundreds of them...')
# st.latex( r \'\'\' e^{i\pi} + 1 = 0 \'\'\')
st.write('Most objects')
st.write(['st', 'is <', 3])
st.header('My Header')
st.subheader('My sub')
st.code('for i in range(8): foo()')


st.title('Display data')

# st.dataframe(my_dataframe)
# st.table(data.iloc[0:10])
st.json({'foo': 'bar', 'fu':'ba'})
st.metric(label="Temp", value = "273 K", delta = '1.2 K')

st.title('Display media')

st.image('./image.jpg')
# st.audio(data)
# st.video(data)