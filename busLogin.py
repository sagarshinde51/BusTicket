import streamlit as st

# Set the title of the application
st.set_page_config(page_title="RFID-Based Bus Ticket System", layout="wide")

# Sidebar for the login page
st.sidebar.title("RFID-Based Bus Ticket System")
st.sidebar.write("Please log in to continue.")

# Login Form in Sidebar
with st.sidebar.form(key="login_form"):
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    login_button = st.form_submit_button("Login")

# Main Page
if login_button:
    if username == "admin" and password == "admin":  # Example credentials
        st.sidebar.success(f"Welcome, {username}!")

        st.title("RFID-Based Bus Ticket System Dashboard")
        st.write("Choose an action below:")

        # Buttons for different actions
        if st.button("Recharge Card"):
            st.subheader("Recharge Card")
            st.write("Here you can recharge RFID cards. (Functionality not implemented yet.)")
            # Add your recharge functionality here

        if st.button("Check Traveled History"):
            st.subheader("Check Traveled History")
            st.write("Here you can check travel history. (Functionality not implemented yet.)")
            # Add your travel history functionality here

        if st.button("View All Users"):
            st.subheader("View All Users")
            st.write("Here is a list of all users. (Functionality not implemented yet.)")
            # Add your user listing functionality here

        # New button to register a passenger
        if st.button("Register Passenger"):
            st.subheader("Register New Passenger")
            with st.form(key="register_passenger_form"):
                name = st.text_input("Name")
                gender = st.selectbox("Gender", ["Male", "Female", "Other"])
                age = st.number_input("Age", min_value=1, max_value=120)
                rfid = st.text_input("RFID")
                balance = st.number_input("Balance", min_value=0.0, step=0.01)
                
                # Upload photo (either from camera or file)
                photo = st.file_uploader("Upload a photo", type=["jpg", "jpeg", "png"])
                if photo is not None:
                    st.image(photo, caption="Uploaded Photo", use_column_width=True)

                # Submit button for registration
                submit_button = st.form_submit_button("Register Passenger")
            
            if submit_button:
                if name and gender and age and rfid and balance and photo:
                    # Process the registration here
                    img_data = photo.read()
                    st.success("Passenger registered successfully!")
                    # Add your data insertion functionality here
                else:
                    st.warning("Please fill out all fields and upload a photo.")

    else:
        st.sidebar.error("Invalid username or password. Please try again.")
else:
    st.write("Please log in from the sidebar to access the system.")
