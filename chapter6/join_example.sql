SELECT 
    users.name,
    user_address.address 
FROM users
JOIN user_address ON users.id = user_address.user_id
