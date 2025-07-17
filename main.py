import streamlit as st
import hashlib
import base64
from hasher import hash_sha256, verify_password
import time

# Page configuration
st.set_page_config(
    page_title="Secure Hash Generator",
    page_icon="🔐",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Custom CSS for better styling
st.markdown("""
<style>
    .main-header {
        background: linear-gradient(90deg, #667eea 0%, #764ba2 100%);
        padding: 1.5rem;
        border-radius: 8px;
        color: white;
        text-align: center;
        margin-bottom: 1rem;
    }
    
    .feature-card {
        background: white;
        padding: 1rem;
        border-radius: 8px;
        border: 1px solid #e0e0e0;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        margin-bottom: 0.5rem;
    }
    
    .hash-display {
        background: #f8f9fa;
        padding: 0.75rem;
        border-radius: 6px;
        border-left: 3px solid #667eea;
        font-family: 'Courier New', monospace;
        word-break: break-all;
        margin: 0.5rem 0;
    }
    
    .success-box {
        background: #d4edda;
        border: 1px solid #c3e6cb;
        border-radius: 6px;
        padding: 0.75rem;
        color: #155724;
        margin: 0.5rem 0;
    }
    
    .error-box {
        background: #f8d7da;
        border: 1px solid #f5c6cb;
        border-radius: 6px;
        padding: 0.75rem;
        color: #721c24;
        margin: 0.5rem 0;
    }
    
    .info-box {
        background: #d1ecf1;
        border: 1px solid #bee5eb;
        border-radius: 6px;
        padding: 0.75rem;
        color: #0c5460;
        margin: 0.5rem 0;
    }
    
    .stButton > button {
        background: linear-gradient(90deg, #667eea 0%, #764ba2 100%);
        color: white;
        border: none;
        border-radius: 20px;
        padding: 0.4rem 1.5rem;
        font-weight: 600;
        transition: all 0.3s ease;
    }
    
    .stButton > button:hover {
        transform: translateY(-1px);
        box-shadow: 0 3px 6px rgba(0,0,0,0.2);
    }
    
    .sidebar .sidebar-content {
        background: linear-gradient(180deg, #667eea 0%, #764ba2 100%);
    }
    
    /* Reduce spacing */
    .block-container {
        padding-top: 1rem;
        padding-bottom: 1rem;
    }
    
    .stTabs [data-baseweb="tab-list"] {
        gap: 0.5rem;
    }
    
    .stTabs [data-baseweb="tab"] {
        padding: 0.5rem 1rem;
    }
</style>
""", unsafe_allow_html=True)

# Sidebar
with st.sidebar:
    st.markdown("""
    <div style="text-align: center; color: white; padding: 0.5rem;">
        <h3>Secure Hash Generator</h3>
        <p style="font-size: 0.9rem;">SHA-256 hashing and password management</p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("---")
    
    st.markdown("**Features:**")
    st.markdown("""
    - SHA-256 Hashing
    - Password Management
    - Salt Support
    - Modern UI
    """)
    
    st.markdown("---")
    
    st.markdown("**Security:**")
    st.markdown("""
    - Client-side processing
    - No data transmission
    - Industry-standard algorithm
    """)

# Main content
st.markdown("""
<div class="main-header">
    <h1>Secure Hash Generator</h1>
    <p>Generate SHA-256 hashes and manage passwords securely</p>
</div>
""", unsafe_allow_html=True)

# Create tabs
tab1, tab2, tab3 = st.tabs(["Hash Generator", "Password Manager", "About"])

with tab1:
    st.markdown("### Generate SHA-256 Hash")
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        input_text = st.text_area(
            "Enter text to hash:",
            placeholder="Type your message here...",
            height=120,
            help="Enter any text to generate its SHA-256 hash"
        )
        
        col_a, col_b = st.columns(2)
        with col_a:
            include_salt = st.checkbox("Add salt", help="Add a random salt for extra security")
        with col_b:
            show_hex = st.checkbox("Show hex format", value=True, help="Display hash in hexadecimal format")
        
        if st.button("Generate Hash", use_container_width=True):
            if input_text:
                with st.spinner("Generating hash..."):
                    time.sleep(0.3)
                    
                    if include_salt:
                        import secrets
                        salt = secrets.token_hex(8)
                        salted_text = input_text + salt
                        hash_result = hash_sha256(salted_text)
                    else:
                        salt = None
                        hash_result = hash_sha256(input_text)
                    
                    st.markdown("**Generated Hash:**")
                    
                    if salt:
                        st.markdown(f"**Salt:** `{salt}`")
                    
                    st.markdown(f"""
                    <div class="hash-display">
                        {hash_result}
                    </div>
                    """, unsafe_allow_html=True)
                    
                    st.code(hash_result, language="text")
                    
                    col_info1, col_info2, col_info3 = st.columns(3)
                    with col_info1:
                        st.metric("Length", f"{len(hash_result)} chars")
                    with col_info2:
                        st.metric("Algorithm", "SHA-256")
                    with col_info3:
                        st.metric("Bits", "256")
            else:
                st.error("Please enter some text to hash.")
    
    with col2:
        st.markdown("### Quick Hash")
        
        quick_options = ["Hello World", "Password123", "admin", "test@email.com"]
        selected_quick = st.selectbox("Select:", quick_options)
        
        if st.button("Quick Hash"):
            quick_hash = hash_sha256(selected_quick)
            st.markdown(f"""
            <div class="hash-display">
                <strong>Input:</strong> {selected_quick}<br>
                <strong>Hash:</strong> {quick_hash[:20]}...
            </div>
            """, unsafe_allow_html=True)

with tab2:
    st.markdown("### Password Management")
    
    if 'stored_password_hash' not in st.session_state:
        st.session_state.stored_password_hash = None
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("**Set New Password**")
        
        new_password = st.text_input(
            "Enter new password:",
            type="password",
            help="Enter a password to store its hash"
        )
        
        confirm_password = st.text_input(
            "Confirm password:",
            type="password",
            help="Re-enter the password to confirm"
        )
        
        if st.button("Store Password Hash", use_container_width=True):
            if new_password and confirm_password:
                if new_password == confirm_password:
                    password_hash = hash_sha256(new_password)
                    st.session_state.stored_password_hash = password_hash
                    
                    st.markdown("""
                    <div class="success-box">
                        Password hash stored successfully!
                    </div>
                    """, unsafe_allow_html=True)
                    
                    st.markdown(f"""
                    <div class="hash-display">
                        {password_hash}
                    </div>
                    """, unsafe_allow_html=True)
                else:
                    st.markdown("""
                    <div class="error-box">
                        Passwords do not match!
                    </div>
                    """, unsafe_allow_html=True)
            else:
                st.error("Please enter both passwords.")
    
    with col2:
        st.markdown("**Verify Password**")
        
        if st.session_state.stored_password_hash:
            verify_input = st.text_input(
                "Enter password to verify:",
                type="password",
                help="Enter the password to verify against stored hash"
            )
            
            if st.button("Verify Password", use_container_width=True):
                if verify_input:
                    is_valid = verify_password(verify_input, st.session_state.stored_password_hash)
                    
                    if is_valid:
                        st.markdown("""
                        <div class="success-box">
                            Password verified successfully!
                        </div>
                        """, unsafe_allow_html=True)
                    else:
                        st.markdown("""
                        <div class="error-box">
                            Password verification failed!
                        </div>
                        """, unsafe_allow_html=True)
                else:
                    st.error("Please enter a password to verify.")
        else:
            st.markdown("""
            <div class="info-box">
                No password hash stored. Please set a password first.
            </div>
            """, unsafe_allow_html=True)
    
    if 'stored_password_hash' in st.session_state and st.session_state.stored_password_hash:
        st.markdown("---")
        col_sec1, col_sec2, col_sec3 = st.columns(3)
        with col_sec1:
            st.metric("Algorithm", "SHA-256")
        with col_sec2:
            st.metric("Length", "64 chars")
        with col_sec3:
            st.metric("Security", "High")

with tab3:
    st.markdown("### About This Application")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        <div class="feature-card">
            <h4>Security Features</h4>
            <ul>
                <li>SHA-256 Algorithm</li>
                <li>Client-side processing</li>
                <li>No data transmission</li>
                <li>Secure hash storage</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
        <div class="feature-card">
            <h4>Features</h4>
            <ul>
                <li>Hash Generation</li>
                <li>Password Management</li>
                <li>Salt Support</li>
                <li>Modern UI</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="feature-card">
            <h4>Use Cases</h4>
            <ul>
                <li>Data Integrity</li>
                <li>Password Storage</li>
                <li>Digital Signatures</li>
                <li>Security Testing</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
        <div class="feature-card">
            <h4>Technology</h4>
            <ul>
                <li>Python 3.8+</li>
                <li>Streamlit Framework</li>
                <li>SHA-256 Algorithm</li>
                <li>Responsive Design</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)

# Footer
st.markdown("---")
st.markdown("""
<div style="text-align: center; color: #666; padding: 0.5rem; font-size: 0.9rem;">
    <p>Built with Streamlit and SHA-256 hashing | Secure • Fast • Beautiful</p>
</div>
""", unsafe_allow_html=True)
