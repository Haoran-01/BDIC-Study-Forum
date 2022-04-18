import { createStore } from 'vuex'
export default createStore({
  //数据管理框架，方便数据多层级传输，创建全局唯一仓库，用来存放全局的数据
  state: {
    //  Home View States
    mainFunctionsVisibility:true,
    //  IndentificationCard States
    Span:false,
    // User Login States
    loginState: false,
    userEmail: null
  },
  getters: {
  },
  mutations: {
  //  Home View Functions
    changeMainFunctionsInvisible(){
      this.state.mainFunctionsVisibility = false;
    },
    changeMainFunctionsVisible(){
      this.state.mainFunctionsVisibility = true;
    },
    changeSpanState(){
      this.Span = !this.Span;
    },
    userLogin(email){
      this.state.loginState = true;
      this.state.userEmail = email;
    },
    userLogout(){
      this.state.loginState = false;
      this.state.userEmail = null;
    }
  },
  actions: {
  },
  modules: {
  }
})