set_user_data(machine_id,
f"""
ssh_authorized_keys:
   - ssh-ecdsa  {public_key}
""")