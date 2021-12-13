<template>
  <vue-autosuggest
    id="pickup-loc"
    :get-suggestion-value="getSuggestionValue"
    :suggestions="suggestions"
    :input-props="{id:'autosuggest__input', onInputChange: getAddresses, placeholder:$store.state.via2_address,
                   autocomplete:'off'}"
    @selected="selected"
    class="form-control p-2"
  >
    <template slot-scope="{suggestion}">
      <i v-if="suggestion.item.formatted" class="fa fa-map-marker dropdown" aria-hidden="true" />
      <i v-else class="fa fa-plane" aria-hidden="true" />
      <span v-if="$store.state.booking_type === 'ToAirport'" class="my-suggestion-item">{{ suggestion.item.name }}</span>

      <span class="my-suggestion-item" v-else>{{ suggestion.item.formatted }}</span>
    </template>
  </vue-autosuggest>
</template>

<script type="text/javascript">
import Vue from 'vue'
export default {
  data() {
    return {
      suggestions: []
    }
  },
  mounted() {
    if (this.$store.state.booking_type === 'ToAirport') {
      Vue.axios.get('/airportplaces/?query=').then((response) => {
        this.suggestions = [response.data]
      })
    }
  },

  methods: {
    getAddresses(text) {
      if (this.$store.state.booking_type === 'ToAirport') {
        Vue.axios.get('/airportplaces/?query=' + text).then((response) => {
          this.suggestions = [response.data]
        })
      } else {
        Vue.axios.get('/addresses/?query=' + text).then((response) => {
          this.suggestions = [response.data]
        })
      }
    },

    getSuggestionValue(suggestion) {
      if (this.$store.state.booking_type === 'ToAirport') {
        return suggestion.item.name
      } else {
        return suggestion.item.formatted
      }
    },

    selected(suggestion) {
      this.$emit('updatevia2', suggestion.item)
      this.$store.dispatch('getQoute')
    }

  }
}
</script>
