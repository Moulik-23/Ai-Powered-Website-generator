import sys
sys.path.insert(0, '.')
from app.models.database import Database

try:
    db = Database.get_database()
    print('✓ MongoDB Atlas connected successfully')
    print(f'Database name: {db.name}')
    if Database.client:
        Database.client.close()
        print('✓ Connection closed')
except Exception as e:
    print(f'✗ Connection failed: {e}')
    sys.exit(1)
