from typing import List
from database.abc.database import IDatabase
from database.database_exceptions import (
    AlreadyClaimedDatabaseException,
    AlreadyExistsDatabaseException,
    NotFoundDatabaseException
)
from database.discount_dto import (
    DiscountDto,
    DeleteDiscountDto,
    ReadDiscountDto,
    UpdateDiscountDto
)
from database.some_database.tables import fake_discounts_table


class SomeDatabase(IDatabase):

    def create_discount(self, new_discount: DiscountDto) -> DiscountDto:
        '''Method to create a discount.'''
        for discount in fake_discounts_table:
            if discount.discountId == new_discount.discountId:
                raise AlreadyExistsDatabaseException("A discount with the given discountId already exists.")
        fake_discounts_table.append(new_discount)
        return new_discount

    def read_discount(self, read_discount: ReadDiscountDto) -> DiscountDto:
        '''Method to read a discount.'''
        for discount in fake_discounts_table:
            if discount.discountId == read_discount.discountId:
                return discount
        raise NotFoundDatabaseException("A discount with the given discountId does not exist.")

    def update_discount(self, update_discount: UpdateDiscountDto) -> DiscountDto:
        '''Method to update a discount.'''
        for discount in fake_discounts_table:
            if discount.discountId == update_discount.discountId:
                if hasattr(discount, 'claimedBy'):
                    raise AlreadyClaimedDatabaseException("The discount Id is already claimed.")
                else:
                    discount.claimedBy = update_discount.claimedBy
                if hasattr(update_discount, 'validFromTime'):
                    discount.validFromTime = update_discount.validFromTime
                if hasattr(update_discount, 'expirationTime'):
                    discount.expirationTime = update_discount.expirationTime
                if hasattr(update_discount, 'isRedeemed'):
                    discount.isRedeemed = update_discount.isRedeemed
                return discount
        raise NotFoundDatabaseException("A discount with the given discountId does not exist.")

    def delete_discount(self, delete_discount: DeleteDiscountDto) -> DiscountDto:
        '''Method to delete a discount.'''
        for discount in fake_discounts_table:
            if discount.discountId == delete_discount.discountId:
                fake_discounts_table.pop(discount)
                return discount
        raise NotFoundDatabaseException("A discount with the given discountId does not exist.")

    def create_batch_discount(self, new_discount_collection: List[DiscountDto]) -> List[DiscountDto]:
        '''Method to create a discount.'''
        response = []
        for new_discount in new_discount_collection:
            try:
                added_discount = self.create_discount(new_discount)
            except AlreadyExistsDatabaseException:
                continue
            response.append(added_discount)
        return response
