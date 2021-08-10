login to redis server:switch to redis-cli then type
-h 127.0.0.1 -p 6379 -a "mypassword"
_commands for redis-cli
DEL :delete key
DUMP: returns serialized version of the value stored at the key
EXIST: check to exist
EXPIREAT key timestamp :Sets the expiry of the key after the specified time. Here time is in Unix timestamp format.
PEXPIRE key milliseconds -Set the expiry of key in milliseconds.

PEXPIREAT key milliseconds-timestamp :Sets the expiry of the key in Unix timestamp specified as milliseconds.

KEYS pattern:Finds all keys matching the specified pattern.

MOVE key db :Moves a key to another database.

1PERSIST key :Removes the expiration from the key.

PTTL key :Gets the remaining time in keys expiry in milliseconds.

TTL key :Gets the remaining time in keys expiry.

RANDOMKEY :Returns a random key from Redis.

RENAME key newkey :Changes the key name.

RENAMENX key newkey :Renames the key, if a new key doesn't exist.

TYPE key :Returns the data type of the value stored in the key.