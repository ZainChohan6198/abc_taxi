import Vue from 'vue'
const getInitialState = () => {
  return {
    hide: false,
    droppoff_id: '',
    pickup_id: '',
    dropoff_address: 'Enter Drop off Location',
    pickup_address: 'Enter Pick up Location',
    pickup_lat: '',
    pickup_lng: '',
    dropoff_lng: '',
    dropoff_lat: '',
    phone: '',
    email: '',
    passengers: '',
    name: '',
    payement_methods: '',
    prebook: '',
    price: '',
    notes: '',
    error: '',
    booking_type: '',
    checked: '',
    pickup_date: '',
    return_date: '',
    booking_status: '',
    vehicle_id: '',
    vehicle_group: '',
    vehicle_type: '',
    loader: false,
    distance: '',
    id: '',
    vehicle_title: '',
    icabbi_status: '',
    via1_id: '',
    via1_address: 'Enter via location',
    via1_lat: '',
    via1_lng: '',
    via2_id: '',
    via2_address: 'Enter via location',
    via2_lat: '',
    via2_lng: '',
    via3_id: '',
    via3_address: 'Enter via location',
    via3_lat: '',
    via3_lng: '',
    driver_name: '',
    driver_lat: null,
    driver_mobile: '',
    driver_lng: null,
    driver_id: '',
    driver_make: '',
    driver_model: '',
    no_plate: ''

  }
}
const state = getInitialState()
export const mutations = {
  resetState(state) {
    Object.assign(state, getInitialState())
  },
  hide(state, hide) {
    state.hide = hide
  },
  dropoff_id(state, dropoff_id) {
    state.droppoff_id = dropoff_id
  },
  dropoff_address(state, dropoff_address) {
    state.dropoff_address = dropoff_address
  },
  dropoff_lat(state, dropoff_lat) {
    state.dropoff_lat = dropoff_lat
  },
  dropoff_lng(state, dropoff_lng) {
    state.dropoff_lng = dropoff_lng
  },
  via1_id(state, via1_id) {
    state.via1_id = via1_id
  },
  via1_address(state, via1_address) {
    state.via1_address = via1_address
  },
  via1_lat(state, via1_lat) {
    state.via1_lat = via1_lat
  },
  via1_lng(state, via1_lng) {
    state.via1_lng = via1_lng
  },
  via2_id(state, via2_id) {
    state.via2_id = via2_id
  },
  via2_address(state, via2_address) {
    state.via2_address = via2_address
  },
  via2_lat(state, via2_lat) {
    state.via2_lat = via2_lat
  },
  via2_lng(state, via2_lng) {
    state.via2_lng = via2_lng
  },
  via3_id(state, via3_id) {
    state.via3_id = via3_id
  },
  via3_address(state, via3_address) {
    state.via3_address = via3_address
  },
  via3_lat(state, via3_lat) {
    state.via3_lat = via3_lat
  },
  via3_lng(state, via3_lng) {
    state.via3_lng = via3_lng
  },
  pickup_address(state, pickup_address) {
    state.pickup_address = pickup_address
  },
  pickup_id(state, pickup_id) {
    state.pickup_id = pickup_id
  },
  pickup_lat(state, pickup_lat) {
    state.pickup_lat = pickup_lat
  },
  pickup_lng(state, pickup_lng) {
    state.pickup_lng = pickup_lng
  },
  name(state, name) {
    state.name = name
  },
  phone(state, phone) {
    state.phone = phone
  },
  price(state, price) {
    state.price = price
  },
  distance(state, distance) {
    state.distance = distance
  },
  notes(state, notes) {
    state.notes = notes
  },
  journey_type(state, journey_type) {
    state.journey_type = journey_type
  },
  email(state, email) {
    state.email = email
  },
  error(state, error) {
    state.error = error
  },
  checked(state, checked) {
    state.checked = checked
  },
  return_date(state, return_date) {
    state.return_date = return_date
  },
  pickup_date(state, pickup_date) {
    state.pickup_date = pickup_date
  },
  booking_status(state, booking_status) {
    state.booking_status = booking_status
  },
  booking_type(state, booking_type) {
    state.booking_type = booking_type
  },

  loader(state, loader) {
    state.loader = loader
  },
  vehicle(state, vehicle) {
    state.vehicle_id = vehicle.id
    state.vehicle_group = vehicle.group
    state.vehicle_type = vehicle.key

    state.passengers = vehicle.seats
  },
  vehicle_title(state, vehicle) {
    state.vehicle_title = vehicle
  },
  id(state, id) {
    state.id = id
  },
  icabbi_status(state, icabbi_status) {
    state.icabbi_status = icabbi_status
  },
  driver(state, driver) {
    state.driver_name = driver.name
    state.driver_mobile = driver.phone
    state.driver_lat = driver.position.lat
    state.driver_lng = driver.position.lng
    state.driver_make = driver.vehicle.make
    state.driver_model = driver.vehicle.model
    state.no_plate = driver.vehicle.reg
    state.driver_id = driver.id
  }

}
const actions = {
  resetState(context) {
    context.commit('resetState')
  },
  getQoute({ commit, state }) {
    const self = this
    if (!state.droppoff_id ||
      !state.pickup_id ||
      !state.vehicle_type) {
    } else if (state.droppoff_id ===
      state.pickup_id) {
      commit('error', 'Pickup and dropoff can never be same place')
    } else {
      commit('loader', true)
      const data = {
        // TODO: Use mapState
        name: state.name,
        pickup_ref: state.pickup_id,
        passenger: state.passengers,
        dropoff_ref: state.droppoff_id,
        phone_number: state.phone,
        vehicle_type: state.vehicle_group,
        dropoff_lat: state.dropoff_lat,
        dropoff_lng: state.dropoff_lng,
        pickup_lat: state.pickup_lat,
        pickup_lng: state.pickup_lng,
        vehicle_title: state.vehicle_title
        // via1_ref: state.via1_id,
        // via1_postcode: state.via1_address,
        // via2_ref: this.state.via2_id,
        // via2_postcode: state.via2_address,
        // via3_ref: this.state.via2_id,
        // via3_postcode: state.via2_address,
      }
      Vue.axios.post('/quotation/', data)
        .then(function (response) {
          commit('loader', false)
          commit('price', response.data.price)
          commit('distance', response.data.distance)
          // self.loading = false
        })
        .catch((error) => {
          commit('loader', false)
          commit('error', error.response.data[0])
          commit('price', '0.00')
        })
    }
  }
}
export default {
  namespaced: true,
  state,
  mutations,
  actions
}
