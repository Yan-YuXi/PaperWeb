import { createStore } from "vuex";

const store = createStore({
    state() {
        return {
            PaperList: [],
            title: '',
            type: '',
            PaperInfo: {}
        }
    },
    mutations: {
        setPaper(state,data) {
            state.PaperList = data["val"]
            state.title = data["input"]
            state.type = data["select"]
        },
        setPaperInfo(state,data) {
            state.PaperInfo = data
        }
    },
    getters: {
        perPagePaper: (state) => (currpage, perpage) => {
            return state.PaperList.slice((currpage-1)*perpage, currpage*perpage)
        }
    }
});
export default store;
