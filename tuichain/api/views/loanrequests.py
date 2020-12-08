from rest_framework.response import Response
from rest_framework.status import (
    HTTP_400_BAD_REQUEST,
    HTTP_403_FORBIDDEN,
    HTTP_404_NOT_FOUND,
    HTTP_200_OK,
    HTTP_201_CREATED,
)
from tuichain.api.models import LoanRequest, Investment
from rest_framework.permissions import *
from rest_framework.decorators import api_view, permission_classes
import decimal

@api_view(["POST"])
@permission_classes((IsAuthenticated,))
def create_loan_request(request):
    """
    Create new LoanRequest
    """
    user = request.user

    school = request.data.get('school')
    course = request.data.get('course')
    amount = request.data.get('amount')

    if school is None or course is None or amount is None:
        return Response({'error': 'Required fields: school, course and amount'},status=HTTP_400_BAD_REQUEST)

    # TODO: verify if User has complete profile and validated identity
    # TODO: add validations to prevent users from creating/having more than one active LoanRequest at a time
    # ...

    loanrequest = LoanRequest.objects.create(student=user, school=school, course=course, amount=amount)
    loanrequest.save()

    return Response({'message': 'Loan Request successfully created'},status=HTTP_201_CREATED)

@api_view(["GET"])
@permission_classes((IsAuthenticated,))
def get_loan_request(request, id):
    """
    Get Loan Request with given ID
    """

    loanrequest = LoanRequest.objects.filter(id=id).first()

    # TODO: should we pass it only if it is validated?

    if loanrequest is None:
        return Response({'error': 'Loan Request with given ID not found'}, status=HTTP_404_NOT_FOUND)

    return Response(
        {
            'message': 'Loan Request found with success', 
            'loan_request': loanrequest.to_dict()
        }, 
        status=HTTP_200_OK
    )

@api_view(["GET"])
@permission_classes((IsAuthenticated,))
def get_personal_loan_requests(request):
    """
    Get Loan Requests made by the authenticated user
    """

    user = request.user

    loanrequest_list = LoanRequest.objects.filter(student=user)

    result = [obj.to_dict() for obj in loanrequest_list]

    return Response(
        {
            'message': 'Loan Requests fetched with success', 
            'loanrequests': result, 
            'count': len(result)
        }, 
        status=HTTP_200_OK
    )


@api_view(["GET"])
@permission_classes((IsAuthenticated,))
def get_all_loan_requests(request):
    """
    Get all active loan requests
    """

    loanrequest_list = LoanRequest.objects.filter(active=True)

    result = [obj.to_dict() for obj in loanrequest_list]

    return Response(
        {
            'message': 'Loan Requests fetched with success', 
            'loanrequests': result, 
            'count': len(result)
        }, 
        status=HTTP_200_OK
    )

@api_view(["GET"])
@permission_classes((IsAuthenticated,))
def get_loan_request_investments(request, id):
    """
    Get investments for a given loan request
    """

    loanrequest = LoanRequest.objects.filter(id=id).first()

    if loanrequest is None:
        return Response({'error': 'Loan Request with given ID not found'}, status=HTTP_404_NOT_FOUND)

    investments = Investment.objects.filter(request=loanrequest)

    result = [obj.to_dict() for obj in investments]

    return Response(
        {
            'message': 'Investments fetched with success for the given Loan Request', 
            'count': len(result),
            'investments': result
        }, 
        status=HTTP_200_OK
    )


    