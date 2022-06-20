<template>
  <div class="form-content">
    <h4 class="mt-2 mb-3">
      Fill the fields to book your taxi
    </h4>
    <div v-if="this.$store.state.error" class="alert alert-danger" role="alert">
      <b>{{ this.$store.state.error }}</b>
    </div>
    <div class="input-group mb-2 mr-sm-2">
      <div class="input-group-prepend">
        <div class="input-group-text">
          From:
        </div>
      </div>
      <!--      <input type="text" class="form-control" placeholder="Pickup Address">-->
      <pickup @updatePickup="updatePickup" />
    </div>
<!--    <div class="via">-->
<!--      <span v-if="!via"><span ><i class="fa fa-plus-circle"  aria-hidden="true" @click="addVia" /></span><span>Via</span></span>-->
<!--      <span v-if="via"><span ><i class="fa fa-times-circle"  aria-hidden="true" @click="closeVia" /></span><span>Via</span></span>-->
<!--    </div>-->
<!--    <div v-if="via || $store.state.via1_id || $store.state.via2_id || $store.state.via3_id" class="">-->
<!--      <div class="input-group mb-2 mr-sm-2 px-2">-->
<!--        <div class="input-group-prepend">-->
<!--          <div class="input-group-text">-->
<!--            Via:-->
<!--          </div>-->
<!--        </div>-->
<!--        &lt;!&ndash;      <input type="text" class="form-control" placeholder="Pickup Address">&ndash;&gt;-->
<!--        <via1 @updatevia1="updatevia1" />-->
<!--      </div>-->
<!--      <div class="input-group mb-2 mr-sm-2 px-2">-->
<!--        <div class="input-group-prepend">-->
<!--          <div class="input-group-text">-->
<!--            Via:-->
<!--          </div>-->
<!--        </div>-->
<!--        &lt;!&ndash;      <input type="text" class="form-control" placeholder="Pickup Address">&ndash;&gt;-->
<!--        <via2 @updatevia2="updatevia2" />-->
<!--      </div>-->
<!--      <div class="input-group mb-2 mr-sm-2 px-2">-->
<!--        <div class="input-group-prepend">-->
<!--          <div class="input-group-text">-->
<!--            Via:-->
<!--          </div>-->
<!--        </div>-->
<!--        &lt;!&ndash;      <input type="text" class="form-control" placeholder="Pickup Address">&ndash;&gt;-->
<!--        <via3 @updatevia3="updatevia3" />-->
<!--      </div>-->
<!--    </div>-->

    <div class="input-group mb-2 mr-sm-2">
      <div class="input-group-prepend">
        <div class="input-group-text">
          To:
        </div>
      </div>
      <dropoff @updateDropoff="updateDropoff" />
    </div>
    <h4>Select Vehicle</h4>
    <div class="vehicle-list">
      <ul>
        <div v-if="!vehicles.length" class="loader vehicle position-static" />
        <li
          v-for="(vehicle) in vehicles"
          :class="{ active: active === vehicle}"
          class=" vehicle-list mb-3"
          @click="selected(vehicle)"
        >
          <div class="vehicle-info text-center p-2 d-flex ">
            <div class="vehicle-img">
              <img alt="businessclass" v-if="vehicle.key === 'R4'" src="../../assets/img/businessclass-car.png">
              <img alt="saloon" v-if="vehicle.key === 'R5'" src="../../assets/img/saloon-car.png">
              <img alt="mvc" v-if="vehicle.key === 'R6'" src="../../assets/img/mpvplus-car.png">
              <img  alt="seven seater" v-if="vehicle.key === 'R7'" src="../../assets/img/seven-seater-car.png">
              <img alt="eight-seater" v-if="vehicle.key === 'R8'" src="../../assets/img/eight-seater-car.png">
              <img alt="estate" v-if="vehicle.key === 'E'" src="../../assets/img/estate-car.png">
              <img alt="saloon" v-if="vehicle.key === 'S'" src="../../assets/img/saloon-car.png">
              <img alt="exuctive car" class="exective"  v-if="vehicle.key === 'X1'" src="../../assets/img/exuctivecar.png">
            </div>
            <div class="active-icon w-50">
              <h4 class="m-0 mb-1">
                <b>{{ vehicle.title }}</b>
              </h4>
              <p class="m-0 mb-1">
                {{ vehicle.description }}
              </p>
              <div class="">
                <div class="d-inline-block">
                  <span class="mr-1">{{ vehicle.luggage }}</span><i class="fa fa-briefcase mr-1" aria-hidden="true" />
                </div>
                <div class="d-inline-block">
                  <span class="mr-1">{{ vehicle.seats }}</span><i class="fa fa-male" aria-hidden="true" />
                </div>
                <div v-if="vehicle.wheelchair" class="d-inline-block">
                  <i class="fa fa-wheelchair-alt ml-1" aria-hidden="true" />
                </div>
              </div>
            </div>
          </div>
        </li>
      </ul>
    </div>
  </div>
</template>
<script>
import Vue from 'vue'
import pickup from '~/components/pickup.vue'
import dropoff from '~/components/dropoff.vue'
import via1 from '~/components/via1.vue'
import via2 from '~/components/via2.vue'
import via3 from '~/components/via3.vue'

export default {
  components: {
    pickup,
    dropoff,
    via1,
    via2,
    via3
  },
  data() {
    return {
      active: '',
      vehicles: [],
      via: false
    }
  },
  computed: {

    pickup_address: {
      get() {
        return this.$store.state.pickup_address
      },
      set(pickup_address) {
        return this.$store.commit('pickup_address', pickup_address)
      }
    },
    pickup_id: {
      get() {
        return this.$store.state.pickup_id
      },
      set(pickup_id) {
        return this.$store.commit('pickup_id', pickup_id)
      }

    },
    pickup_lat: {
      get() {
        return this.$store.state.pickup_lat
      },
      set(pickup_lat) {
        return this.$store.commit('pickup_lat', pickup_lat)
      }
    },
    pickup_lng: {
      get() {
        return this.$store.state.pickup_lng
      },
      set(pickup_lng) {
        this.$store.commit('pickup_lng', pickup_lng)

      }
    },
    dropoff_address: {
      get() {
        return this.$store.state.droppoff_address
      },
      set(dropoff_address) {
        return this.$store.commit('dropoff_address', dropoff_address)
      }
    },
    dropoff_id: {
      get() {
        return this.$store.state.dropoff_id
      },
      set(dropoff_id) {
        return this.$store.commit('dropoff_id', dropoff_id)
      }

    },
    dropoff_lat: {
      get() {
        return this.$store.state.dropoff_lat
      },
      set(dropoff_lat) {
        return this.$store.commit('dropoff_lat', dropoff_lat)
      }
    },
    dropoff_lng: {
      get() {
        return this.$store.state.dropoff_lng
      },
      set(dropoff_lng) {
        this.$store.commit('dropoff_lng', dropoff_lng)
      }
    },
    via1_address: {
      get() {
        return this.$store.state.via1_address
      },
      set(via1_address) {
        return this.$store.commit('via1_address', via1_address)
      }
    },
    via1_id: {
      get() {
        return this.$store.state.via1_id
      },
      set(via1_id) {
        return this.$store.commit('via1_id', via1_id)
      }

    },
    via1_lat: {
      get() {
        return this.$store.state.via1_lat
      },
      set(via1_lat) {
        return this.$store.commit('via1_lat', via1_lat)
      }
    },
    via1_lng: {
      get() {
        return this.$store.state.via1_lng
      },
      set(via1_lng) {
        this.$store.commit('via1_lng', via1_lng)
      }
    },
    via2_address: {
      get() {
        return this.$store.state.via2_address
      },
      set(via2_address) {
        return this.$store.commit('via2_address', via2_address)
      }
    },
    via2_id: {
      get() {
        return this.$store.state.via2_id
      },
      set(via2_id) {
        return this.$store.commit('via2_id', via2_id)
      }

    },
    via2_lat: {
      get() {
        return this.$store.state.via2_lat
      },
      set(via2_lat) {
        return this.$store.commit('via2_lat', via2_lat)
      }
    },
    via2_lng: {
      get() {
        return this.$store.state.via2_lng
      },
      set(via2_lng) {
        this.$store.commit('via2_lng', via2_lng)
      }
    },
    via3_address: {
      get() {
        return this.$store.state.via3_address
      },
      set(via3_address) {
        return this.$store.commit('via3_address', via3_address)
      }
    },
    via3_id: {
      get() {
        return this.$store.state.via3_id
      },
      set(via3_id) {
        return this.$store.commit('via3_id', via3_id)
      }

    },
    via3_lat: {
      get() {
        return this.$store.state.via3_lat
      },
      set(via3_lat) {
        return this.$store.commit('via3_lat', via3_lat)
      }
    },
    via3_lng: {
      get() {
        return this.$store.state.via3_lng
      },
      set(via3_lng) {
        this.$store.commit('via3_lng', via3_lng)
      }

    }
  },
  mounted() {
    const self = this
    Vue.axios.get('/vehicletypes/')
      .then(function (response) {
        self.vehicles = response.data.data
      })
      .catch(() => {
        this.$store.commit('error', 'No vehicle available at the moment')
      })
  },
  methods: {
    addVia() {
      this.via = true
    },
    closeVia() {
      this.via = false
    },

    selected(vehicle) {
      this.active = vehicle
      this.$store.commit('vehicle', vehicle)
      this.$store.commit('vehicle_title', vehicle.title)
      this.$store.dispatch('getQoute')
    },
    updatePickup(suggestion) {
      this.pickup_address = suggestion.formatted
      this.pickup_id = suggestion.id
      this.pickup_lat = suggestion.lat
      this.pickup_lng = suggestion.lng
    },
    updateDropoff(suggestion) {
      this.dropoff_address = suggestion.formatted
      this.dropoff_id = suggestion.id
      this.dropoff_lat = suggestion.lat
      this.dropoff_lng = suggestion.lng
    },
    updatevia1(suggestion) {
      this.via1_address = suggestion.formatted
      this.via1_id = suggestion.id
      this.via1_lat = suggestion.lat
      this.via1_lng = suggestion.lng
    },
    updatevia2(suggestion) {
      this.via2_address = suggestion.formatted
      this.via2_id = suggestion.id
      this.via2_lat = suggestion.lat
      this.via2_lng = suggestion.lng
    },
    updatevia3(suggestion) {
      this.via3_address = suggestion.formatted
      this.via3_id = suggestion.id
      this.via3_lat = suggestion.lat
      this.via3_lng = suggestion.lng
    }

  }
}
</script>
