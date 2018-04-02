# from rest_framework import permissions
# from company.models import Company
# from seller.models import Seller
#
#
# class InCompany(permissions.BasePermission):
#     message = "You not in this company"
#
#     def has_permission(self, request, view):
#             try:
#                 company_id = view.kwargs['company_id']
#                 company = Company.objects.get(pk=company_id)
#                 company.sellers.get(pk=request.user.seller.id)
#                 return True
#             except (Seller.DoesNotExist, Company.DoesNotExist):
#                 return False
#             except KeyError:
#                 return True
#
#
