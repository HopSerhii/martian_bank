

import { createSlice } from "@reduxjs/toolkit";

const initialState = {
  applied_loan: [],
  loan_history: [],
  isLoading: false,
  error: null,
};

const loanSlice = createSlice({
  name: "loan",
  initialState,
  reducers: {
    createLoan: (state, action) => {
      state.applied_loan = action.payload;
    },
    storeLoanHistory: (state, action) => {
      state.loan_history = action.payload;
    },
  },
});

export const { createLoan, storeLoanHistory } = loanSlice.actions;

export default loanSlice.reducer;
