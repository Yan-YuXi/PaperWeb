import { createStore } from "vuex";

const store = createStore({
    state() {
        return {
            PaperList: [],
            title: '',
            type: '',
            PaperInfo: {},
            paperPath: '',
            fileName: '',
            isEqual: ''
        }
    },
    mutations: {
        setPaper(state,data) {
            state.PaperList = data["val"]
            state.title = data["input"]
            state.type = data["select"]
            state.isEqual = data["isequal"]
        },
        setPaperInfo(state,data) {
            state.PaperInfo = data
        },
        setPaperPath(state, data) {
            state.paperPath = data['path']
            state.fileName = data['name']
        }
    },
    getters: {
        perPagePaper: (state) => (currpage, perpage) => {
            return state.PaperList.slice((currpage-1)*perpage, currpage*perpage)
        }
    }
});
export default store;
