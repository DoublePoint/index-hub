function getStart(){
  const start = new Date();
  start.setTime(start.getTime() - 3600 * 1000 * 24 * 7);
  return start;
}

const indexes = {
  namespaced: true,
  state: {
    indexName:[],
    startDate:getStart(),
    endDate:new Date()
  },

  mutations: {
    SET_INDEX_NAME: (state, indexName) => {
      state.indexName = indexName
    },
    PUSH_INDEX_NAME: (state, indexName) => {
      state.indexName.push(indexName);
    },
    UNSHIFT_INDEX_NAME: (state, indexName) => {
      state.indexName.unshift(indexName);
    },
    REMOVE_INDEX_NAME: (state, indexName) => {
      const index = state.indexName.indexOf(indexName);
      state.indexName.splice(index,1);
      // state.indexName.push(indexName);
    },
    SET_START_DATE: (state, startDate) => {
      state.startDate = startDate
    },
    SET_END_DATE: (state, endDate) => {
      state.endDate = endDate
    },
  },

  actions: {
    setIndexName({ commit },indexName) {
      commit('SET_INDEX_NAME',indexName)
    },
    pushIndexName({ commit },indexName) {
      commit('PUSH_INDEX_NAME',indexName)
    },
    unshiftIndexName({ commit },indexName) {
      commit('UNSHIFT_INDEX_NAME',indexName)
    },
    removeIndexName({ commit },indexName) {
      commit('REMOVE_INDEX_NAME',indexName)
    },
    setIndexStartDate({ commit },startDate) {
      commit('SET_START_DATE',startDate)
    },
    setIndexEndDate({ commit },endDate) {
      commit('SET_END_DATE',endDate)
    },
  }
}

export default indexes
