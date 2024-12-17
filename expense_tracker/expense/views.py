from rest_framework import generics
from rest_framework.response import Response
from .models import Expense
from .serializers import ExpenseSerializer
from datetime import datetime
from django.db.models import Sum


class ExpenseListCreateView(generics.ListCreateAPIView):
    serializer_class = ExpenseSerializer

    def get_queryset(self):
        queryset = Expense.objects.all()

        user_id = self.request.query_params.get("user_id", None)
        if user_id is not None:
            queryset = queryset.filter(user_id=user_id)

        return queryset


class ExpenseDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Expense.objects.all()
    serializer_class = ExpenseSerializer


class ExpenseByDateRangeView(generics.ListAPIView):
    serializer_class = ExpenseSerializer

    def get_queryset(self):
        user_id = self.request.query_params.get("user_id")
        start_date = self.request.query_params.get("start_date")
        end_date = self.request.query_params.get("end_date")

        if not user_id or not start_date or not end_date:
            return Expense.objects.none()

        try:
            start_date = datetime.strptime(start_date, "%Y-%m-%d").date()
            end_date = datetime.strptime(end_date, "%Y-%m-%d").date()
        except ValueError:
            return Expense.objects.none()

        return Expense.objects.filter(
            user_id=user_id, date__range=[start_date, end_date]
        )


class CategorySummaryView(generics.GenericAPIView):
    def get(self, request):
        user_id = request.query_params.get("user_id")
        month = request.query_params.get("month")

        if not user_id or not month:
            return Response({"error": "user_id and month are required"}, status=400)

        try:
            month = datetime.strptime(month, "%Y-%m").date()
        except ValueError:
            return Response({"error": "Invalid month format. Use YYYY-MM."}, status=400)

        expenses = Expense.objects.filter(
            user_id=user_id, date__year=month.year, date__month=month.month
        )
        category_summary = expenses.values("category").annotate(
            total_amount=Sum("amount")
        )

        return Response(category_summary)
