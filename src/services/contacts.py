from typing import List, Optional
from sqlalchemy.ext.asyncio import AsyncSession

from src.repository.contacts import ContactRepository
from src.schemas import ContactModel
from src.database.models import Contact, User


class ContactService:
    def __init__(self, db: AsyncSession):
        self.repository = ContactRepository(db)

    async def create_contact(self, body: ContactModel, user: User):
        return await self.repository.create_contact(body, user)

    async def get_contacts(
        self,
        user: User,
        skip: int = 0,
        limit: int = 100,
        name: Optional[str] = None,
        lastname: Optional[str] = None,
        email: Optional[str] = None,
    ) -> List[Contact]:
        return await self.repository.get_contacts(
            user, skip, limit, name, lastname, email
        )

    async def get_contact(self, contact_id: int, user: User):
        return await self.repository.get_contact_by_id(contact_id, user)

    async def update_contact(self, contact_id: int, body: ContactModel, user: User):
        return await self.repository.update_contact(contact_id, body, user)

    async def remove_contact(self, contact_id: int, user: User):
        return await self.repository.remove_contact(contact_id, user)

    async def get_upcoming_birthdays(self, user: User) -> List[Contact]:
        return await self.repository.get_upcoming_birthdays(user)
