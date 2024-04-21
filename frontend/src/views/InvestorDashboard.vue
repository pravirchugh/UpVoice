<template>
<div class="dashboard-link">
      <router-link to="/investor/dashboard" :class="{ active: activeLink === 'Requests received' }" @click="setActiveLink('investor/dashboard')">Requests received</router-link>
    <router-link to="/investor/visualization" :class="{ active: activeLink === 'Visualizations' }" @click="setActiveLink('Visualizations')">Visualizations</router-link>
</div>
  <div class="investor-requests">
    <h2>Requests Raised by Citizens</h2>
    <div class="card no-hover">
      <DataTable :value="requests" :editingRows="editingRows" dataKey="id" @row-edit-save="onRowEditSave" stripedRows>
      <Column field="id" header="Request ID" style="width: 15%"></Column>
      <Column field="citizenName" header="Citizen Name" style="width: 20%"></Column>
      <Column field="category" header="Category" style="width: 20%"></Column>
      <Column field="description" header="Description" style="width: 30%"></Column>
      <Column field="status" header="Status" style="width: 15%">
  <template #body="slotProps">
    <template v-if="slotProps.editing">
      <Dropdown v-model="slotProps.data[slotProps.field]" 
                :options="statuses" 
                optionLabel="label" 
                optionValue="value" 
                placeholder="Select a Status">
        <template #option="optionProps">
          <Tag :value="optionProps.option.value" :severity="getStatusLabel(optionProps.option.value)" />
        </template>
      </Dropdown>
    </template>
    <template v-else>
      <Tag :value="slotProps.data.status" :severity="getStatusLabel(slotProps.data.status)" />
    </template>
  </template>
  <template #editor="slotProps">
    <Button icon="pi pi-pencil" class="p-button-rounded p-button-text" @click="slotProps.toggleEdit()"/> 
  </template>
</Column>
    </DataTable>
    </div>
  </div>
</template>

<script>
import { ref } from 'vue';
import DataTable from 'primevue/datatable';
import Column from 'primevue/column';

export default {
  components: {
    DataTable,
    Column
  },
    data() {
    return {
      activeLink: 'Requests received'
    };
  },
  methods: {
    setActiveLink(link) {
      this.activeLink = link;
    }
  },
  setup() {
    const requests = ref([
      {
        id: 1,
        citizenName: 'John Doe',
        category: 'Healthcare',
        description: 'Request for medical assistance',
        status: 'Pending'
      },
      {
        id: 2,
        citizenName: 'Jane Smith',
        category: 'Healthcare',
        description: 'Irregular composition of C2H4',
        status: 'Approved'
      },
      {
        id: 3,
        citizenName: 'John Doe',
        category: 'Healthcare',
        description: 'Request for better facility',
        status: 'Pending'
      },
      {
        id: 4,
        citizenName: 'Jane Smith',
        category: 'Healthcare',
        description: 'Non availability of Dolo',
        status: 'Approved'
      },
      {
        id: 5,
        citizenName: 'John Doe',
        category: 'Healthcare',
        description: 'Request for medical assistance',
        status: 'Rejected'
      },
      {
        id: 6,
        citizenName: 'Jane Smith',
        category: 'Healthcare',
        description: 'X-A1 dosage side effects',
        status: 'Approved'
      },
      // Add more request objects as needed
    ]);

    const editingRows = ref([]);

    const statuses = [
      { label: 'Pending', value: 'Pending' },
      { label: 'Approved', value: 'Approved' },
      { label: 'Rejected', value: 'Rejected' }
    ];

    const getStatusLabel = status => {
      switch (status) {
        case 'Pending':
          return 'warning';
        case 'Approved':
          return 'success';
        case 'Rejected':
          return 'danger';
        default:
          return 'info';
      }
    };

    const onRowEditSave = event => {
      // Handle row edit save event
    };

    return { requests, editingRows, statuses, getStatusLabel, onRowEditSave };
  }
};
</script>

<style scoped>
.investor-requests {
  margin: 20px;
}

.dashboard-link {
  display: flex;
  justify-content: center;
  margin-top: 50px; /* Adjust as needed */
}

.dashboard-link a {
  margin: 0 10px;
  padding: 10px 20px;
  text-decoration: none;
  border-radius: 5px;
  background-color: #551a8b; /* Change color as needed */
  color: #fff;
}

.dashboard-link a.active {
  background-color: #551a8b; /* Change color for active link */
}

.card {
  border-radius: 5px;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
  padding: 20px;
  background-color: #fff;
  width: 100%;
}

.no-hover:hover {
  transform: none !important;
  transition: none !important;
}

.p-datatable {
  border: none;
  margin-top: 20px; 
}
</style>
