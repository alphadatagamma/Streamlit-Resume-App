mkdir -p ~/.streamlit/
echo “\
[general]\n\
email = \”abhishek.2.gupta@uconn.edu\”\n\
“ > ~/.streamlit/credentials.toml
echo “\
[server]\n\
headless = true\n\
enableCORS=false\n\
port = $PORT\n\
“ > ~/.streamlit/config.toml