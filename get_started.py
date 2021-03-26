import streamlit as st
import numpy as np
import pandas as pd
import altair as alt

st.set_page_config(page_title="Streamlit Getting Started Guide", initial_sidebar_state="expanded")

options = ("🏃‍♀️Getting Started",
    "⬇️ Installing Streamlit",
    "🏗 Basic Functions",
    "🎨 Layout and Themes",
    "🏎 App Performance",
    "🚀 Deploying your App",
    "🎈 More Resources")

nav = st.sidebar.selectbox("Choose a section", options)
st.sidebar.write(nav)

if nav == options[0]:
    """
    # Getting Started with Streamlit
    Welcome to Streamlit! Streamlit is an open-source framework for easily creating web apps in Python.
    Whether you want to show off your machine learning model, build an advanced analytics app, or create an internal tool, you can quickly make your app with Streamlit.

    Check out some examples and templates or go to [streamlit.io/gallery](streamlit.io/gallery) to browse many more.
    ##
    """

    # img_col1, img_col2, img_col3 = st.beta_columns(3)
    #
    # with img_col1:
    #     st.image("images/apps/demo-uber.png", width=225)
    #     st.markdown(
    #         f'<p align=center><a href="https://share.streamlit.io/streamlit/demo-uber-nyc-pickups/">Browse NYC Uber data</a></p>',
    #         unsafe_allow_html=True,
    #     )
    #
    # with img_col2:
    #     st.image("images/apps/demo-gan.png", width=225)
    #     st.markdown(
    #         f'<p align=center><a href="https://share.streamlit.io/streamlit/demo-face-gan">Try out a GAN</a></p>',
    #         unsafe_allow_html=True,
    #     )
    #
    # with img_col3:
    #     st.image("images/apps/demo-themes.png", width=225)
    #     st.markdown(
    #         f'<p align=center><a href="https://share.streamlit.io/streamlit/theming-showcase/main">See theming examples</a></p>',
    #         unsafe_allow_html=True,
    #     )

    # """
    # ### Templates
    # """

    template_col1, template_col2, template_col3 = st.beta_columns(3)

    with template_col1:
        st.image("images/apps/basic.png", width=225)
        st.markdown(
            f'<p align=center><a href="https://share.streamlit.io/kellyamanda/templates/main/template_basic.py">Basic layout with sidebar</a></p>',
            unsafe_allow_html=True,
        )

    with template_col2:
        st.image("images/apps/wide.png", width=225)
        st.markdown(
            f'<p align=center><a href="https://share.streamlit.io/kellyamanda/templates/main/template_wide.py">Wide mode layout</a></p>',
            unsafe_allow_html=True,
        )
    with template_col3:
        st.image("images/apps/demo-themes.png", width=225)
        st.markdown(
            f'<p align=center><a href="https://share.streamlit.io/streamlit/theming-showcase/main">Theming examples</a></p>',
            unsafe_allow_html=True,
        )
    # with template_col3:
    #     st.image("images/apps/explainer.png", width=225)
    #     st.markdown(
    #         f'<p align=center><a href="https://share.streamlit.io/kellyamanda/templates/main/template_explainer.py">Explanation style layout</a></p>',
    #         unsafe_allow_html=True,
    #     )

    """
    ##
    Ready to get set up? Click below for instructions on installing Streamlit. ⬇️
    """
    st.button("Next > Install Streamlit")

if nav == options[1]:
    """
    # Installing the Streamlit library
    ##
    """

    install_col1, install_col2, install_col3 = st.beta_columns(3)
    install_code = "pip install streamlit"

    with install_col1:
        st.image("images/icons/windows.png", width=57)
        st.subheader("Windows")
        st.write("Some words about Windows and link to troubleshooting")
        st.code(install_code, language="bash")

    with install_col2:
        st.image("images/icons/mac.jpeg", width=78)
        st.subheader("Mac")
        st.write("Some words about Mac and link to troubleshooting")
        st.code(install_code, language="bash")

    with install_col3:
        st.image("images/icons/linux.png", width=50)
        st.subheader("Linux")
        st.write("Some words about Linux and link to troubleshooting")
        st.code(install_code, language="bash")

    """
    #
    Ready to get into the code? Click below to learn about basic Streamlit functions. 🏗
    """
    st.button("Next > Basic Functions")

if nav == options[2]:
    """
    # Streamlit's basic functions
    There's a way to do just about anything you want with Streamlit, but here we'll introduce you
    to the basics of text, data, widgets, and visualizations. For more complex examples poke around on the
    [Streamlit forum](discuss.streamlit.io).

    ## Text
    Your basic functions for text are `st.title`, `st.header`, `st.subtitle`, and `st.write`.
    You can also use specialized functions like `st.markdown`, `st.text`, `st.code`, or `st.latex`. Here are some examples.
    """

    with st.echo():
        st.subheader("Here's a subheader")
        st.write("Here's some regular text with **bolding**")

    """
    #
    ## Data

    The easiest way to write data is just to use the `st.write` function. You can also use `st.table` or `st.dataframe` for different layouts.
    """

    with st.echo():
        df = pd.DataFrame({
          'first column': [1, 2, 3, 4],
          'second column': [10, 20, 30, 40]
        })
        st.write(df)

    """
    #
    ## Visualizing Data

    So much data visualization! For charts there are some basic functions in Streamlit color_picker `st.line_chart`
    and `st.map`, but Streamlit also supports Altair, PyPlot, Vega Lite, Plotly, Bokeh, PyDeck, Seaborn and more.
    Check out the docs for [all the charting types](https://docs.streamlit.io/en/stable/api.html?highlight=number_input#display-charts).
    """
    with st.echo():
        df = pd.DataFrame(
            np.random.randn(200, 3),
            columns=['a', 'b', 'c'])

        st.subheader("Basic line chart")
        st.line_chart(df)
        st.subheader("Altair chart")
        c = alt.Chart(df).mark_circle().encode(
            x='a', y='b', size='c', color='c', tooltip=['a', 'b', 'c'])
        st.altair_chart(c, use_container_width=True)

    """
    #
    ## Widgets

    Get your app interactive! Widgets are the core of building a great app. Streamlit offers a large number of widgets including
    `st.button`, `st.checkbox`, `st.radio`, `st.selectbox`, `st.multiselect`, `st.slider`, `st.text_input`, `st.date_input`, `st.number_input`, and [many more](https://docs.streamlit.io/en/stable/api.html#display-interactive-widgets).

    To use widgets, you just make a new variable and assign the value from the widget to it. Then you can use that to manipulate things in your app.
    """

    with st.echo():
        number = st.slider("select a number",1,100)
        emoji = st.selectbox("select emojis",("🍩","🦊","🎈","🐳"))
        result = number * emoji
        st.write("You have asked for ",number,"of ", emoji,": ")
        st.write(result)

    """
    #
    ## Media

    Use `st.image`, `st.video`, and `st.audio` to quickly add media to your app.
    """

    with st.echo():
        st.subheader("Images")
        st.image("https://rb.gy/2kdyzg")

        st.subheader("Videos")
        st.video("https://www.youtube.com/watch?v=IwOfCgkyEj0")

    """
    #
    Now that you know the basics, let's get into app layout and customization 🎨
    """
    st.button("Next > Layout and Themes")

if nav == options[3]:
    """
    # Layout and Theming for your Streamlit app
    Now that you've mastered the basic functions, it's time to take your app to the next level by adding layout and themes.

    ## Sidebar
    The Sidebar is a great option for persistent text or controls for your app. To move something to the sidebar just append `st.sidebar` in front
    of the function. Expand the sidebar to the left to see the controls we have for this app.

    """
    st.code("""
        nav = st.sidebar.selectbox("Choose a section",
            ("Getting Started",
            "Installing Streamlit",
            "Basic Functions",
            "Layout and Themes",
            "Performance"
            "Deploying your App",
            "More Resources"))
        """,
        language="python")

    """
    (A word of warning... while you can put an infinite amount of things in the sidebar, if you have a lot of
    controls or text you probably want to consider another layout! See more below.)

    ## Columns and Grid Layout
    Columns are your go to layout option when you want to display things side by side or in a grid.
    This is a great option for displaying a lot of widgets at the top of your app or for displaying a number of charts or data next to one another.

    """
    with st.echo():
        df = pd.DataFrame(
            np.random.randn(200, 3),
            columns=['a', 'b', 'c'])

        st.subheader("Widget layout example")

        a1, a2, a3 = st.beta_columns(3)

        with a1:
            st.multiselect("Choose data", ["a", "b", "c"])
            st.slider("Select value",1,100)

        with a2:
            st.number_input("Select number", 1,10)
            st.text_input("Add text")

        with a3:
            st.date_input("Select date")
            st.time_input("Pick a time")

        st.subheader("Chart layout example")

        b1, b2 = st.beta_columns((2,1)) # use this notation to specify relative widths of columns

        with b1:
            st.area_chart(df)
        with b2:
            st.write (df)

    """
    #
    ## Themes
    You Streamlit app will default to the Light Mode you see here unless you otherwise specify a theme. While you're
    developing you can simply go to the hamburger menu in the upper right, select Settings, and then choose if you want to
    switch to Dark Mode or create your own theme by choosing various colors and fonts. You can also set the them
    directly in your config file. Here's an [example app with different themes](https://share.streamlit.io/streamlit/theming-showcase/main),
    and [documentation on changing the theme](https://docs.streamlit.io/en/stable/theme_options.html).
    """

    st.image("images/theming.gif")

    """

    ## Wide Mode, Page Title, Favicons and More
    As a final customization, you can use `st.set_page_config` to change default aspects of your app like the layout (wide or centered) and the
    default state of the sidebar (auto, expanded, or collapsed). For this app we have made it wide mode with the sidebar collapsed. You can also
    use `st.set_page_config` to set a custom page title or favicon. Note that for `st.set_page_config` to work, it must be the very first Streamlit
    function that you call in your app. Here is the page configuration we use for this app:

    """

    st.code("""
        st.set_page_config(page_title="Streamlit Getting Started Guide", initial_sidebar_state="collapsed")
        """, language="python")

    """
    #
    Now that you have a great looking app, let's move on to improving your app's performance. 🏎
    """
    st.button("Next > Performance")

if nav == options[4]:
    """
    # Optimizing for app performance
    Your app looks good but it also needs to load and update quickly. Streamlit apps run just like Python scripts - from top to bottom - which
    means that anytime something changes in your app, like a widget changing a value, the whole script reruns. Streamlit does magic behind
    the scenes to make this run fast by default, but there are a few things you should do to help speed it up.

    ## @st.cache
    Any time you are loading in data, manipulating large datasets, or performing extensive computations you should think about creating a function
    and using the `@st.cache` decorator to store results in the local cache. That way the next time you call the cached function, Streamlit will
    skip executing the function and just returned the previously stored output. Which all makes your app much faster!

    Here is an example using ``@st.cache`:
    """

    st.code("""
    @st.cache
    def expensive_computation(a, b):
        time.sleep(2)  # This makes the function take 2s to run
        return a * b

    a = 2
    b = 21
    res = expensive_computation(a, b)

    st.write("Result:", res)

    """, language="python")

    """

    Note: `@st.cache` only works on functions. So make sure to put your data pull or computation in a function before using `@st.cache`.
    [Read more about @st.cache](https://docs.streamlit.io/en/stable/caching.html) in our documentation.

    ## Using buttons and forms
    Sometimes you have a lot of widgets and you want to wait until everything has been adjusted and entered before running the computation.
    In that case `st.button` and `st.beta_form` are going to be your best friends.

    MORE STUFF HERE

    ## Code clean up
    If after that your app is still running slowly, something someting about cleaning up your code for production... don't load in 10000 pandas rows....

    ADD IN STATE LATER ON

    """

    """
    #
    If you're app is running well, then now it's time to deploy and share it!  🚀
    """
    st.button("Next > Deploying your app")

if nav == options[5]:
    """
    # Deploying your App
    You've made an app and now you're ready to share it. Congrats! Streamlit offers a free deployment platform called [Streamlit Sharing](https://streamlit.io/sharing)
    that you can use to deploy any public apps in a matter of minutes. Just host your app in a public GitHub repo, log in to Streamlit Sharing, and get your app deployed
    in one click! If you need secure, private deployment then try [Streamlit for Teams](https://streamlit.io/for-teams).

    """

    st.image("images/deploy_large.gif")

    """
    You can also host apps yourself on your preferred platform and there are many resources online about how to containerize your app and deploy on Heroku, AWS, GCP, or Azure.

    Now you're all set! Click forward for more resources and happy Streamlit-ing!  🎈
    """
    st.button("Next > More Resources")

if nav == options[6]:
    """
    # More Resources and Inspiration
    Docs
    Gallery
    Forum
    """
